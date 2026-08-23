# The database lives at the very top, outside of any loops or functions.
cars = {
    "Porsche Macan": 85000,
    "Porsche 911 Gt3": 190000,
    "Mercedes G-Class": 160000,
    "Mercedes S-Class": 120000,
    "Bmw M5": 130000,
    "Bmw X6": 95000,
    "Audi Rs6": 125000,
    "Audi R8": 165000,
    "Range Rover Autobiography": 145000,
    "Aston Martin Vantage": 155000,
    "Lamborghini Urus": 230000,
    "Ferrari Roma": 210000
}

# 1. THE TOOL: It does exactly ONE thing. No loops, no exits.
def check_inventory(car_model, max_budget):
    """
    Looks up a car in the inventory and evaluates if the customer's budget is sufficient.
    """
    # Direct dictionary lookup! We don't need a 'for' loop because we 
    # already verified the car exists before calling this function.
    car_price = cars[car_model]
    
    if max_budget >= car_price:
        print(f"Match found! The {car_model} is available for €{car_price}. Let's book a test drive.")
    else:
        shortfall = car_price - max_budget
        print(f"The {car_model} costs €{car_price}. You need €{shortfall} more to afford this vehicle.")

# 2. THE ENGINE: It handles the loop, user input, and all the "Exit" or "Continue" logic.
def main():
    while True:
        try:
            inp1 = input("What car are you looking for? (or type 'exit' to quit): ").title()

            # The break lives here, safely inside the while loop!
            if inp1 == "Exit":
                print("Shutting down the terminal. Have a great day!")
                break
            
            # The continue lives here, safely inside the while loop!
            if inp1 not in cars:
                print(f"Sorry. We do not have {inp1} in stock right now. Please check again later!")
                continue

            inp2 = int(input("What is your maximum budget in Euros? "))

        except ValueError:
            print("Invalid response. Please try again!")
            continue

        # If the code survives the checks above, it calls your specialized tool!
        check_inventory(inp1, inp2)

if __name__ == "__main__":
    main()
    
            


