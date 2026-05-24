import json


def convert_response_time(value):

    if value.endswith("ms"):
        return float(value.replace("ms", ""))

    elif value.endswith("s"):
        return float(value.replace("s", "")) * 1000

    else:
        return float(value)


def parse_line(line):

    line = line.strip()

    if line == "":
        return None

    if line.startswith("{"):

        try:

            data = json.loads(line)

            return {
                "timestamp": data["timestamp"],
                "ip": data["ip"],
                "method": data["method"],
                "path": data["path"],
                "status": data["status"],
                "response_time": convert_response_time(data["response_time"])
            }

        except:
            return None

    parts = line.split()

    if len(parts) < 6:
        return None

    try:

        timestamp = parts[0]
        ip = parts[1]
        method = parts[2]
        path = parts[3]

        if parts[4] == "-":
            status = "MISSING"
        else:
            status = parts[4]

        response_time = convert_response_time(parts[5])

        return {
            "timestamp": timestamp,
            "ip": ip,
            "method": method,
            "path": path,
            "status": status,
            "response_time": response_time
        }

    except:
        return None