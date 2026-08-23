#First Project-VIP Budget Filter
print("Welcome to Voluntari Luxury Motors.")
try:
    budget = float(input("Please enter your maximum budget in Euros:"))
except ValueError:
    print("Invalid input. Please enter numbers only, without commas or letters.")
print("Processing your profile...")

if budget < 50000 and budget >= 15000:
    print(f"Based on your budget of €{budget}, we recommend the Mercedes C-Class.")
elif budget >= 50000 and budget < 100000:
    print(f"Based on your budget of €{budget}, we recommend the Porsche Macan.")
else:
    print(f"Based on your budget of €{budget}, we recommend the Porsche GT3-RS.")

