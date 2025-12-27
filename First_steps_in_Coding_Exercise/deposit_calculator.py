# Input: principal amount, months of deposit, and annual interest rate
deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate_percent = float(input())

# Convert annual rate to decimal and calculate monthly interest
monthly_interest = (deposit_amount * (annual_interest_rate_percent / 100)) / 12

# Total amount calculation: Principal + (Months * Monthly Interest)
total_amount = deposit_amount + (term_of_deposit * monthly_interest)

print(total_amount)
