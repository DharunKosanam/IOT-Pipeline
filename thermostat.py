import time
import json
import random
import boto3
import os
from datetime import datetime


device_id = "thermostat_1"

base_temp = 21.0

s3_bucket_name = os.getenv("S3_BUCKET_NAME")
if not s3_bucket_name:
    raise ValueError("S3_BUCKET_NAME environment variable not set")

s3_client = boto3.client('s3')

print(f"Starting thermostat simulation for device: {device_id}")
print(f"Uploading data to S3 bucket: {s3_bucket_name}")

while True:
    try:
        temp_fluc = random.uniform(-0.5, 0.5)
        current_temp = round(base_temp + temp_fluc, 2)

        timestamp = datetime.utcnow().isoformat()

        data = {
            'device_id': device_id,
            'timestamp': timestamp,
            'temperature': current_temp
        }

        json_data = json.dumps(data)

        file_name = f"data_{timestamp}.json"

        s3_client.put_object(Bucket="dharun-thermostat-data", Key=file_name, Body=json_data)

        print(f"Uploaded {file_name} to S3")

        time.sleep(5)

    except KeyboardInterrupt:
        print("Thermostat stopped.")
        break
    except Exception as e:
        print(f"Error occurred: {e}")
        break