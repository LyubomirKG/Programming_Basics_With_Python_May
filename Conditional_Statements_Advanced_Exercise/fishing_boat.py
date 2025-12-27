# Constants for seasonal boat rental prices
SPRING_PRICE = 3000
SUMMER_AUTUMN_PRICE = 4200
WINTER_PRICE = 2600

# User input: budget, season, and number of fishermen
budget = int(input())
season = input()
number_fishers = int(input())

price_for_rent = 0

# Determine base price based on the season
if season == 'Spring':
    price_for_rent = SPRING_PRICE
elif season == 'Summer' or season == 'Autumn':
    price_for_rent = SUMMER_AUTUMN_PRICE
else:
    price_for_rent = WINTER_PRICE

# Apply group size discounts
if number_fishers <= 6:
    price_for_rent *= 0.90  # 10% discount
elif 7 <= number_fishers <= 11:
    price_for_rent *= 0.85  # 15% discount
else:
    price_for_rent *= 0.75  # 25% discount

# Additional 5% discount for even number of fishers (excluding Autumn)
if season != 'Autumn' and number_fishers % 2 == 0:
    price_for_rent *= 0.95

# Final result output
if budget >= price_for_rent:
    print(f'Yes! You have {budget - price_for_rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {price_for_rent - budget:.2f} leva.')
