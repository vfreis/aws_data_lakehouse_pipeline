import requests
import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")

BUCKET = "data-lakehouse-demo"


def fetch_api_data():

    url = "https://api.sampleapis.com/coffee/hot"
    response = requests.get(url)

    return response.json()


def save_to_bronze(data):

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

    key = f"bronze/coffee_data/{timestamp}.json"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data)
    )

    print(f"Saved to Bronze Layer: {key}")


if __name__ == "__main__":
    data = fetch_api_data()
    save_to_bronze(data)