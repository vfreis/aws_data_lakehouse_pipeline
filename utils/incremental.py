import boto3

s3 = boto3.client("s3")

def get_last_processed(bucket, key):

    try:
        obj = s3.get_object(Bucket=bucket, Key=key)
        return obj["Body"].read().decode()
    except:
        return None