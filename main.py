from parser import parse_line

file_name = input("Enter log file name: ")

total_lines = 0
good_lines = 0
bad_lines = 0

endpoint_count = {}
status_count = {}

slowest_endpoint = ""
slowest_time = 0

file = open(file_name, "r")

for line in file:

    total_lines += 1

    result = parse_line(line)

    if result is None:

        bad_lines += 1

    else:

        good_lines += 1

        path = result["path"]
        status = result["status"]
        response_time = result["response_time"]

        if path in endpoint_count:
            endpoint_count[path] += 1
        else:
            endpoint_count[path] = 1

        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1

        if response_time > slowest_time:
            slowest_time = response_time
            slowest_endpoint = path

file.close()

print("\n========== REPORT ==========\n")

print("Total lines:", total_lines)
print("Good lines:", good_lines)
print("Bad lines:", bad_lines)

print("\nEndpoint Counts:")

for endpoint in endpoint_count:
    print(endpoint, ":", endpoint_count[endpoint])

print("\nStatus Counts:")

for status in status_count:
    print(status, ":", status_count[status])

print("\nSlowest Endpoint:")
print(slowest_endpoint, "-", slowest_time, "ms")