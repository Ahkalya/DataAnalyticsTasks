from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower, regexp_replace, to_date, coalesce, lit
from pyspark.sql.types import StringType

def clean_transactions(input_path, output_path):
    spark = SparkSession.builder.appName("CleanTransactions").getOrCreate()
    df = spark.read.option("header", True).csv(input_path)

    print("Initial Data Sample :")
    df.show(5)

    # Clean all string columns (trim and lower)
    for column in df.columns:
        if isinstance(df.schema[column].dataType, StringType):
            df = df.withColumn(column, lower(trim(col(column))))

    # Clean city and bank_name
    df = df.withColumn("city", regexp_replace(col("city"), r"[^a-zA-Z\s]", ""))
    df = df.withColumn("bank_name", regexp_replace(col("bank_name"), r"[^a-zA-Z\s]", ""))

    # Clean and cast amount
    df = df.withColumn("amount", regexp_replace(col("amount").cast("string"), r"[^\d.]", ""))
    df = df.withColumn("amount", col("amount").cast("float"))

    # Handle multiple date formats
    df = df.withColumn("transaction_date",
        coalesce(
            to_date(col("transaction_date"), "yyyy/MM/dd"),
            to_date(col("transaction_date"), "dd-MM-yyyy"),
            to_date(col("transaction_date"), "dd.MM.yyyy"),
            to_date(col("transaction_date"), "dd-MMM-yyyy")
        )
    )

    # Drop only rows where essential columns are null
    df = df.dropDuplicates()
    df = df.na.drop(subset=["transaction_id", "transaction_date", "amount"])

    print("Cleaned Data Sample:")
    df.show(5)

    df.coalesce(1).write.mode("overwrite").option("header", True).csv("gs://ahkalya-bucket_project/cleaned_data/")


if __name__ == "__main__":
    input_path = "gs://ahkalya-bucket_project/merged_transactions_clean/"
    output_path = "gs://ahkalya-bucket_project/cleaned_data/sample_transactions_clean"
    clean_transactions(input_path, output_path)
