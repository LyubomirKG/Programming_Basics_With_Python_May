# User input for projection type and hall dimensions
projection_type = input()
rows = int(input())
cols = int(input())

# Determine the ticket price based on the type of projection
if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5.00
else:
    price = 0.00

# Calculate total income based on seating capacity and ticket price
total_income = rows * cols * price

# Output the result formatted to 2 decimal places
print(f"{total_income:.2f} leva")
