flower_type = input()
flower_count = int(input())
budget = int(input())

price_per_flower = 0

# Define base price based on flower type
if flower_type == "Roses":
    price_per_flower = 5
elif flower_type == "Dahlias":
    price_per_flower = 3.80
elif flower_type == "Tulips":
    price_per_flower = 2.80
elif flower_type == "Narcissus":
    price_per_flower = 3
elif flower_type == "Gladiolus":
    price_per_flower = 2.50

# Calculate initial total price
total_price = flower_count * price_per_flower

# Apply discounts or price increases based on quantity
if flower_type == "Roses" and flower_count > 80:
    total_price *= 0.90  # 10% discount
elif flower_type == "Dahlias" and flower_count > 90:
    total_price *= 0.85  # 15% discount
elif flower_type == "Tulips" and flower_count > 80:
    total_price *= 0.85  # 15% discount
elif flower_type == "Narcissus" and flower_count < 120:
    total_price *= 1.15  # 15% price increase
elif flower_type == "Gladiolus" and flower_count < 80:
    total_price *= 1.20  # 20% price increase

# Calculate the difference between budget and total cost
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
