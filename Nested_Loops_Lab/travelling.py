# Travel savings tracker using nested while loops
while True:
    destination = input()
    
    # Exit condition for the entire program
    if destination == "End":
        break

    required_budget = float(input())
    current_savings = 0.0

    # Accumulate savings until the budget goal is reached
    while current_savings < required_budget:
        deposit = float(input())
        current_savings += deposit

    # Success message once the inner loop condition is met
    print(f"Going to {destination}!")
