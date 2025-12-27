# Pricing constants
PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

# Discount and Rent constants
BULK_DISCOUNT_THRESHOLD = 50
DISCOUNT_PERCENT = 0.25
RENT_PERCENT = 0.10

# Input: vacation cost and quantity of each toy type
vacation_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

# Total quantity and initial total price
total_quantity = (number_puzzles + number_dolls + number_teddy_bears + 
                  number_minions + number_trucks)

total_sales = ((number_puzzles * PUZZLE_PRICE)
                + (number_dolls * DOLL_PRICE)
                + (number_teddy_bears * TEDDY_BEAR_PRICE)
                + (number_minions * MINION_PRICE)
                + (number_trucks * TRUCK_PRICE))

# Apply 25% discount if 50 or more toys are ordered
if total_quantity >= BULK_DISCOUNT_THRESHOLD:
    total_sales -= (total_sales * DISCOUNT_PERCENT)

# Deduct 10% for store rent
final_profit = total_sales * (1 - RENT_PERCENT)

# Output result: check if profit covers vacation cost
if final_profit >= vacation_price:
    print(f'Yes! {final_profit - vacation_price:.2f} lv left.')
else:
    print(f'Not enough money! {vacation_price - final_profit:.2f} lv needed.')
