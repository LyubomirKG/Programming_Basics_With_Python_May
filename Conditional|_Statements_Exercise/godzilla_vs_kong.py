# Constants for easy maintenance
DECOR_PERCENTAGE = 0.10
CLOTHES_DISCOUNT_THRESHOLD = 150
CLOTHES_DISCOUNT_PERCENTAGE = 0.10

# Input: budget, number of extras (statists), and clothing cost per extra
budget_movie = float(input())
number_statists = int(input())
clothes_price_per_statist = float(input())

# Basic calculations
decor_price = budget_movie * DECOR_PERCENTAGE
total_clothes_price = number_statists * clothes_price_per_statist

# Apply discount if the number of extras is above the threshold
if number_statists > CLOTHES_DISCOUNT_THRESHOLD:
    total_clothes_price -= (total_clothes_price * CLOTHES_DISCOUNT_PERCENTAGE)

total_needed_money = decor_price + total_clothes_price

# Final budget validation and output
if total_needed_money > budget_movie:
    print('Not enough money!')
    print(f'Wingard needs {total_needed_money - budget_movie:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget_movie - total_needed_money:.2f} leva left.')
