import boto3

emr = boto3.client("emr")

CLUSTER_ID = "j-XXXXXXXX"

def submit_spark_step():

    response = emr.add_job_flow_steps(
        JobFlowId=CLUSTER_ID,
        Steps=[
            {
                "Name": "Silver Transformation",
                "ActionOnFailure": "CONTINUE",
                "HadoopJarStep": {
                    "Jar": "command-runner.jar",
                    "Args": [
                        "spark-submit",
                        "s3://scripts/silver_transformation.py"
                    ],
                },
            }
        ],
    )

    return response