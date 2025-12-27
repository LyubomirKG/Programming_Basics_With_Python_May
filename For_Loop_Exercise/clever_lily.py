# Input: age, price of the washing machine, and price of a single toy
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
toys_count = 0
current_money_gift = 10  # Money gift starts at 10 for the 2nd birthday
stolen_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        # Even birthdays: get money, but brother takes 1 lv.
        money_saved += current_money_gift
        current_money_gift += 10
        stolen_money += 1
    else:
        # Odd birthdays: get a toy
        toys_count += 1

# Total calculation
total_from_toys = toys_count * toy_price
final_savings = (money_saved + total_from_toys) - stolen_money

difference = abs(final_savings - washing_machine_price)

# Final verdict
if final_savings >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
