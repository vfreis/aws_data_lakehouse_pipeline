"""Bronze -> Silver sample transformation for the public portfolio.

The sample API stores a JSON array in S3, so Spark reads it using multiLine.
This is a snapshot demo (overwrite), NOT a transactional incremental pipeline.
"""

from __future__ import annotations

import argparse
import logging
import os

LOGGER = logging.getLogger(__name__)
DEFAULT_BRONZE = "s3://data-lakehouse-demo/bronze/coffee_data/"
DEFAULT_SILVER = "s3://data-lakehouse-demo/silver/coffee_data/"
REQUIRED_FIELDS = ("id", "title", "description", "ingredients")


def transform(spark, bronze_path: str, silver_path: str) -> None:
    """Read snapshots, reject incomplete schema and create a Silver snapshot.

    overwrite is for reproducible portfolio demos only. It is not atomic and
    does not implement CDC, MERGE, watermark management or safe retries.
    """
    source = spark.read.option("multiLine", "true").json(bronze_path)
    missing = set(REQUIRED_FIELDS) - set(source.columns)
    if missing:
        raise ValueError("Missing Bronze fields: " + ", ".join(sorted(missing)))

    # Keep data distributed. Avoid toPandas(), which collects to the driver.
    silver = source.select(*REQUIRED_FIELDS).dropDuplicates(["id"])
    silver.write.mode("overwrite").parquet(silver_path)
    LOGGER.info("Silver snapshot written to %s", silver_path)


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Coffee API Bronze-to-Silver demo")
    parser.add_argument("--bronze-path", default=os.getenv("BRONZE_PATH", DEFAULT_BRONZE))
    parser.add_argument("--silver-path", default=os.getenv("SILVER_PATH", DEFAULT_SILVER))
    args = parser.parse_args(argv)

    from pyspark.sql import SparkSession

    logging.basicConfig(level=logging.INFO)
    spark = SparkSession.builder.appName("BronzeToSilverPortfolio").getOrCreate()
    try:
        transform(spark, args.bronze_path, args.silver_path)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
