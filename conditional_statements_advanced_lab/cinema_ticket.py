# Map days of the week to their respective ticket prices
ticket_prices = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16
}

# Input: day of the week
day_of_week = input()

# Retrieve price based on input, handling potential invalid entries
if day_of_week in ticket_prices:
    print(ticket_prices[day_of_week])
else:
    # Optional: handle cases where input is not a valid day
    pass
