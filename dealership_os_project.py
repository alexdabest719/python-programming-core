import csv


def calculate_financing(price, down_payment, months, interest_rate):
    principal_amount = price - down_payment

    if interest_rate == 0:
        payment = principal_amount/months
        return round(payment, 2)

    
    monthly_rate = (interest_rate/100) / 12
    payment = principal_amount * ((monthly_rate * (1 + monthly_rate) ** months)/((1 + monthly_rate) ** months - 1))

    return round(payment, 2)

def parse_vendor_string(raw_string):
    make, model, price, doors = raw_string.split(",")

    return {"Make": make.strip(),
            "Model": model.strip(),
            "Price": float(price.strip()),
            "Doors": int(doors.strip())
            }


def export_inventory(inventory_list, filename = "inventory.csv"):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["Make", "Model", "Price"])

        writer.writeheader()

        for inventory in inventory_list:
            row_dict = {
                "Make": inventory.make,
                "Model": inventory.model,
                "Price": inventory.price
            }

            writer.writerow(row_dict)
            

    return True

class Vehicle:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if float(price) < 1000:
            raise ValueError("Insufficient funds")

        self._price = float(price)

    def __str__(self):
        return f"{self.make} {self.model} - ${self._price}"

class Car(Vehicle):
    def __init__(self, make, model, price, doors):
        super().__init__(make, model, price)
        self.doors = doors

    @classmethod
    def from_string(cls, raw_string):
        string = raw_string.split(",")
        company = string[0]
        model_name = string[1]
        pricetag = float(string[2])
        num_of_doors =  int(string[3])

        return cls(company, model_name, pricetag, num_of_doors)



class Truck(Vehicle):
    def __init__(self, make, model, price, towing_capacity):
        super().__init__(make, model, price)
        self.towing_capacity = towing_capacity


class Dealership:
    def __init__(self):
        self.inventory = []

    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)

    def show_inventory(self):
        for vehicle in self.inventory:
            print(vehicle)

def main():
    my_dealership = Dealership()
    while True:
        print("\n=== DEALERSHIP OS MAIN MENU ===")
        print("1. Add a new Car")
        print("2. Add a new Truck")
        print("3. Scan raw Vendor String (Car)")
        print("4. View Inventory")
        print("5. Close OS")
        print("6. Calculate Financing")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            print("\n-- Enter Car Details --")
            make = input("Make: ")
            model = input("Model: ")
            price = input("Price: ")
            doors = input("Doors: ")

            try:
                car = Car(make, model, price, doors)
                my_dealership.add_vehicle(car)
                print("✅ Car successfully added to inventory.")
            except ValueError as e:
                print(f"❌ Error building car: {e}")

        elif choice == "2":
            print("\n-- Enter Truck Details --")
            make = input("Make: ")
            model = input("Model: ")
            price = input("Price: ")
            towing = input("Towing capacity: ")

            try:
                truck = Truck(make, model, price, towing)
                my_dealership.add_vehicle(truck)
                print("✅ Truck successfully added to inventory.")
            except ValueError as e:
                print(f"❌ Error building car: {e}")

        elif choice == "3":
            raw_data = input("\nPaste raw vendor string (e.g. Toyota,Camry,25000,4):")

            try:
                clean_data = parse_vendor_string(raw_data)
                scanned_car = Car(clean_data["Make"], clean_data["Model"], clean_data["Price"], clean_data["Doors"])
                my_dealership.add_vehicle(scanned_car)
                print("✅ Barcode scanned and car added.")
            except Exception:
                print("❌ Invalid string format. Try again.")

        elif choice == "4":
            print("\n--- CURRENT INVENTORY ---")
            my_dealership.show_inventory()

        elif choice == "5":
            export_inventory(my_dealership.inventory)
            print("✅ Inventory saved to inventory.csv.")
            print("Thank you for using Dealership OS! Have a nice day")
            break

        elif choice == "6":
            print("\n-- Financing Calculator --")
            try:
                price = float(input("Car Price: "))
                down = float(input("Down Payment: "))
                months = int(input("Months (e.g., 60): "))
                rate = float(input("Interest Rate (e.g., 5.0): "))

                payment = calculate_financing(price, down, months, rate)
                print(f"✅ Estimated Monthly Payment: ${payment}")

            except ValueError:
                print("❌ Invalid number entered.")


        else:
            print("Invalid option. Please try again")
            continue

if __name__== "__main__":
    main()



        



        

    
        