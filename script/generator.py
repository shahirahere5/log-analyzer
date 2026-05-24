import random
import json
import time

methods = ["GET", "POST", "PUT", "DELETE"]

paths = [
    "/api/users",
    "/api/login",
    "/api/orders",
    "/api/products"
]

statuses = [200, 201, 400, 401, 404, 500]

user_agents = [
    "Mozilla/5.0",
    "Chrome/123",
    "PostmanRuntime",
    "Safari/17"
]

file = open("generated.log", "w")

for i in range(1000):

    random_type = random.randint(1, 8)

    if random_type == 1:

        line = (
            "2024-03-15T14:23:01Z "
            + "192.168.1."
            + str(random.randint(1, 255))
            + " "
            + random.choice(methods)
            + " "
            + random.choice(paths)
            + " "
            + str(random.choice(statuses))
            + " "
            + str(random.randint(10, 500))
            + "ms\n"
        )

        file.write(line)

    elif random_type == 2:

        line = (
            "15-Mar-2024 14:23:01 "
            + "10.0.0."
            + str(random.randint(1, 255))
            + " "
            + random.choice(methods)
            + " "
            + random.choice(paths)
            + " "
            + str(random.choice(statuses))
            + " "
            + str(random.randint(1, 2))
            + "s\n"
        )

        file.write(line)

    elif random_type == 3:

        line = (
            str(int(time.time()))
            + " "
            + "172.16.0."
            + str(random.randint(1, 255))
            + " "
            + random.choice(methods)
            + " "
            + random.choice(paths)
            + " "
            + str(random.choice(statuses))
            + " "
            + str(random.randint(50, 300))
            + "\n"
        )

        file.write(line)

    elif random_type == 4:

        line = (
            "2024-03-15T14:23:01Z "
            + "192.168.1."
            + str(random.randint(1, 255))
            + " "
            + random.choice(methods)
            + " "
            + random.choice(paths)
            + " - "
            + str(random.randint(10, 500))
            + "ms\n"
        )

        file.write(line)

    elif random_type == 5:

        line = (
            "2024-03-15T14:23:01Z "
            + "192.168.1."
            + str(random.randint(1, 255))
            + " "
            + random.choice(methods)
            + " "
            + random.choice(paths)
            + " "
            + str(random.choice(statuses))
            + " "
            + str(random.randint(10, 500))
            + "ms "
            + "\""
            + random.choice(user_agents)
            + "\"\n"
        )

        file.write(line)

    elif random_type == 6:

        data = {
            "timestamp": "2024-03-15T14:23:01Z",
            "ip": "192.168.1." + str(random.randint(1, 255)),
            "method": random.choice(methods),
            "path": random.choice(paths),
            "status": random.choice(statuses),
            "response_time": str(random.randint(10, 500)) + "ms"
        }

        file.write(json.dumps(data) + "\n")

    elif random_type == 7:

        file.write("BROKEN LOG ENTRY HERE\n")

    else:

        file.write("\n")

file.close()

print("generated.log created")