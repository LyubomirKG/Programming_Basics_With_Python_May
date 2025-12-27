# Constants for room pricing
ROOM_PRICES = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}

# Input: duration of stay, accommodation type, and customer feedback
days = int(input())
room_type = input()
review = input()

# Calculate actual nights (staying N days means N-1 nights)
nights = days - 1
total_price = nights * ROOM_PRICES[room_type]

# Apply volume discounts based on room type and length of stay
if room_type == "apartment":
    if days < 10:
        total_price *= 0.70  # 30% discount
    elif 10 <= days <= 15:
        total_price *= 0.65  # 35% discount
    else:
        total_price *= 0.50  # 50% discount

elif room_type == "president apartment":
    if days < 10:
        total_price *= 0.90  # 10% discount
    elif 10 <= days <= 15:
        total_price *= 0.85  # 15% discount
    else:
        total_price *= 0.80  # 20% discount

# Adjust final price based on the quality of service review
if review == "positive":
    total_price *= 1.25  # 25% increase for positive feedback
elif review == "negative":
    total_price *= 0.90  # 10% decrease for negative feedback

# Output the final calculated price
print(f"{total_price:.2f}")
