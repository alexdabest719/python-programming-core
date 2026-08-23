# The Dealership CSV Loader

import csv
import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments. Type the file again, please!")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments. Type the file again, please!")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("This file is not a CSV file. Please use another file")
else:
    file_name = sys.argv[1]
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file, fieldnames=["make", "model", "price", "year"])
            for car in reader:
                        print(f"{car["year"]} {car["make"]} {car["model"]} - ${car["price"]}")


    except FileNotFoundError:
        sys.exit("File not found. Please choose an according file")

        
