# Input: number of elements to sum
n = int(input())

# Accumulator variable
total_sum = 0

# Loop through the inputs and add each to the total
for _ in range(n):
    current_number = int(input())
    total_sum += current_number

# Final result
print(total_sum)
