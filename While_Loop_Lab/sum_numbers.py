# Accumulator algorithm reaching a predefined target sum
target_value = int(input())
current_total_sum = 0

# Continue reading numbers until the total meets or exceeds the target
while current_total_sum < target_value:
    input_number = int(input())
    current_total_sum += input_number

# Final output of the accumulated sum
print(current_total_sum)
