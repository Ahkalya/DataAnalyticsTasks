from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim

spark = SparkSession.builder.appName("FilterFailed").getOrCreate()

# Load cleaned data
df = spark.read.option("header", True).csv("gs://ahkalya-bucket_project/cleaned_data/")

# Normalize status column
df_clean = df.withColumn("status", lower(trim(col("status"))))

# Filter rows where status = 'failure'
failed_df = df_clean.filter(col("status") == "failure")

#  Save the failed transactions
failed_df.write.mode("overwrite").option("header", True).csv("gs://ahkalya-bucket_project/failed_data/")
