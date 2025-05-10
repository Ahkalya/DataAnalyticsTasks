from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("MergeDirtyCSVs").getOrCreate()

#Input and Output GCS Paths
input_path = "gs://ahkalya-bucket_project/branch_city_csv/*"
output_path = "gs://ahkalya-bucket_project/merged_transactions_clean/"

# Read all CSVs from the input path
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Optional: Drop rows where all values are null (common in dirty data)
df_clean = df.dropna(how="all")

# Optional: Drop duplicates if necessary
df_clean = df_clean.dropDuplicates()

# Save merged & cleaned CSV to output GCS path
df_clean.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

# Stop the Spark session
spark.stop()
