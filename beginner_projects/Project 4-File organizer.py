import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Invalid file type")

file1 = sys.argv[1]
file2 = sys.argv[2]
cars = []

try:
    with open(file1, "r", newline="") as file:
        reader = csv.DictReader(file)  # Assumes CSV has a header line
        for row in reader:
            price = float(row["price"])
            if price < 100000:
                price *= 1.05
            
            cars.append({
                "make": row["make"],
                "model": row["model"],
                "price": price,
                "year": row["year"]
            })

except FileNotFoundError:
    sys.exit("File not found")
else:
    with open(file2, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["make", "model", "price", "year"])
        writer.writeheader()
        writer.writerows(cars)
