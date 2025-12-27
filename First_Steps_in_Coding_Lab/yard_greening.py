# Constants for pricing
PRICE_PER_SQUARE_METER = 7.61
DISCOUNT_PERCENTAGE = 0.18

# Input: total square meters to be landscaped
sq_meters = float(input())

# Calculate base price and discount amount
base_price = sq_meters * PRICE_PER_SQUARE_METER
discount_amount = base_price * DISCOUNT_PERCENTAGE

# Final calculation
final_price = base_price - discount_amount

# Display results
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_amount} lv.')
