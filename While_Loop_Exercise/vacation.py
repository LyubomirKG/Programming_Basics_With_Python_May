# Financial discipline tracker (Saving vs Spending)
goal_amount = float(input())
current_balance = float(input())

total_days = 0
spend_streak = 0

while True:
    action = input()  # "spend" or "save"
    amount = float(input())
    total_days += 1

    if action == "spend":
        spend_streak += 1
        current_balance -= amount
        # Ensure balance doesn't drop below zero
        if current_balance < 0:
            current_balance = 0
    elif action == "save":
        # Reset the streak on any saving action
        spend_streak = 0
        current_balance += amount

    # Check for failure condition: 5 consecutive days of spending
    if spend_streak == 5:
        print("You can't save the money.")
        print(total_days)
        break

    # Check for success condition: goal reached
    if current_balance >= goal_amount:
        print(f"You saved the money for {total_days} days.")
        break
