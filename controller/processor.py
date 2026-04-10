def process_data(data):
    alert = False

    if data["cpu"] > 80 or data["memory"] > 80:
        alert = True

    return {
        "node": data["node"],
        "cpu": data["cpu"],
        "memory": data["memory"],
        "alert": alert
    }
