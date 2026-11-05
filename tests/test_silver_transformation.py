"""Fast, AWS-free contract tests for the public PySpark portfolio example."""

from unittest.mock import MagicMock
import pytest
from spark_jobs.silver_transformation import transform


def test_silver_transform_reads_multiline_json_and_keeps_spark_distributed():
    spark = MagicMock()
    source = spark.read.option.return_value.json.return_value
    source.columns = ["id", "title", "description", "ingredients"]

    transform(spark, "s3://test/bronze", "s3://test/silver")

    spark.read.option.assert_called_once_with("multiLine", "true")
    spark.read.option.return_value.json.assert_called_once_with("s3://test/bronze")
    source.select.assert_called_once_with("id", "title", "description", "ingredients")
    source.select.return_value.dropDuplicates.assert_called_once_with(["id"])
    source.select.return_value.dropDuplicates.return_value.write.mode.assert_called_once_with("overwrite")
    source.select.return_value.dropDuplicates.return_value.write.mode.return_value.parquet.assert_called_once_with("s3://test/silver")
    assert not source.toPandas.called


def test_missing_schema_fails_before_write():
    spark = MagicMock()
    source = spark.read.option.return_value.json.return_value
    source.columns = ["id", "title"]
    with pytest.raises(ValueError, match="description, ingredients"):
        transform(spark, "s3://test/bronze", "s3://test/silver")
    source.select.assert_not_called()
