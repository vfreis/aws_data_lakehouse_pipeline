from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from ai_layer.llm_enrichment import enrich_with_llm

pandas_df = clean_df.toPandas()

enriched_df = enrich_with_llm(pandas_df)

final_df = spark.createDataFrame(enriched_df)

spark = SparkSession.builder \
    .appName("BronzeToSilver") \
    .getOrCreate()

bronze_path = "s3://data-lakehouse-demo/bronze/coffee_data/"
silver_path = "s3://data-lakehouse-demo/silver/coffee_data/"

df = spark.read.json(bronze_path)

clean_df = df.select(
    col("title"),
    col("description"),
    col("ingredients")
)

clean_df.write \
    .mode("overwrite") \
    .parquet(silver_path)

print("Silver Layer successfully created")