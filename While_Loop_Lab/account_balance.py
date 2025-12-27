# Real-time bank account balance tracker
total_balance = 0.0

while True:
    input_line = input()
    
    # Check for completion command
    if input_line == "NoMoreMoney":
        break

    deposit_amount = float(input_line)
    
    # Validate transaction (negative deposits are not allowed)
    if deposit_amount < 0:
        print("Invalid operation!")
        break
    else:
        # Update total balance and notify user
        total_balance += deposit_amount
        print(f"Increase: {deposit_amount:.2f}")

# Final report
print(f"Total: {total_balance:.2f}")
