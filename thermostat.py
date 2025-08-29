import time
import json
import random
from datetime import datetime


device_id = "thermostat_1"

base_temp = 21.0

print(f"Starting thermostat simulation for device: {device_id}")

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

        print(json.dumps(data))

        time.sleep(5)

    except KeyboardInterrupt:
        print("Thermostat stopped.")
        break