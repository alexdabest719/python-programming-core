#Second Project-The Inventory Matrix



while True:

    try:



        cars = {

            "Porsche Macan": 85000,

            "Porsche 911 GT3": 190000,

            "Mercedes G-Class": 160000,

            "Mercedes S-Class": 120000,

            "BMW M5": 130000,

            "BMW X6": 95000,

            "Audi RS6": 125000,

            "Audi R8": 165000,

            "Range Rover Autobiography": 145000,

            "Aston Martin Vantage": 155000,

            "Lamborghini Urus": 230000,

            "Ferrari Roma": 210000

        }



        inp1 = str(input("What car are you looking for? (or type 'exit' to quit): ")).title()

        inp2 = int(input("What is your maximum budget in Euros? "))



    except ValueError:

        print("Invalid response. Please try again!")

        continue



    else:



        if inp1 == "Exit":

            print("Shutting down the terminal. Have a great day!")

            break



        if inp1 not in cars.keys():

            print(f"Sorry. We do not have {inp1} in stock right now. Please check again later!")

            continue

       

        for item in cars:

            if item == inp1:

                if inp2 >= cars[item]:

                    print(f"Match found! The {item} is available for {cars[item]}. Let's book a test drive.")



                else:

                    shortfall = cars[item] - inp2

                    print(f"The {item} costs {cars[item]}. You need {shortfall} more to afford this vehicle")