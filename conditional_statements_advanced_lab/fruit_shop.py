# Input: product name, day of the week, and quantity
fruit = input()
day = input()
quantity = float(input())

# Pricing for weekdays
weekday_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

# Pricing for weekends
weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

# Determine the correct price list based on the day of the week
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    price_list = weekday_prices
elif day in ["Saturday", "Sunday"]:
    price_list = weekend_prices
else:
    # Handle invalid day input
    print("error")
    exit()

# Check if the fruit exists in the selected price list and calculate total
if fruit in price_list:
    total = price_list[fruit] * quantity
    print(f"{total:.2f}")
else:
    # Handle invalid fruit input
    print("error")
