# Input: number of elements per side (total elements will be 2 * n)
n = int(input())

left_sum = 0
right_sum = 0

# Iterate through all 2*n numbers
for i in range(2 * n):
    current_num = int(input())
    
    # Split the input into two groups based on the index
    if i < n:
        left_sum += current_num
    else:
        right_sum += current_num

# Compare results
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
