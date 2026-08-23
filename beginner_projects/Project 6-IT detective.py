import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Invalid file type")
else:

    try:
        inp = sys.argv[1]
        oup = sys.argv[2]

        logs = []

        with open(inp, "r", newline= "") as file:
            reader = csv.DictReader(file, fieldnames= ["timestamp", "status_code", "server_name", "message"])
            for row in reader:
                if row["status_code"].startswith("5"):
                    logs.append(row)

    except FileNotFoundError:
        sys.exit("File not found.")

    else:
        with open(oup, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["timestamp", "server_name", "status_code", "message"])
            writer.writeheader()
            writer.writerows(logs)