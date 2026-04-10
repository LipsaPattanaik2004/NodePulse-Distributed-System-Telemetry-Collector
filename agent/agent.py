import time
import requests
import psutil
import socket

CONTROLLER_URL = "http://controller:5000/ingest"

def collect_metrics():
    return {
        "node": socket.gethostname(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent
    }

while True:
    data = collect_metrics()
    try:
        response = requests.post(CONTROLLER_URL, json=data)
        print("Sent:", data, "Response:", response.status_code)
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(5)
