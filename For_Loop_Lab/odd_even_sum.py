# Input: number of integers to follow
n = int(input())

even_position_sum = 0
odd_position_sum = 0

for i in range(n):
    current_number = int(input())
    
    # Logic: range(n) starts from index 0
    # Index 0 is considered the 1st position (odd)
    # Index 1 is considered the 2nd position (even)
    if i % 2 == 0:
        odd_position_sum += current_number
    else:
        even_position_sum += current_number

# Result analysis
if odd_position_sum == even_position_sum:
    print("Yes")
    print(f"Sum = {odd_position_sum}")
else:
    diff = abs(odd_position_sum - even_position_sum)
    print("No")
    print(f"Diff = {diff}")
