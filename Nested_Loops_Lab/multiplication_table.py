# Generates a standard 10x10 multiplication table
# Outer loop for the first factor (rows)
for i in range(1, 11):
    # Inner loop for the second factor (columns)
    for j in range(1, 11):
        # Calculate and print the product
        result = i * j
        print(f"{i} * {j} = {result}")
