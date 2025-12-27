# Input: number of elements to follow
n = int(input())

# Initialize an empty list and populate it with input integers
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# Find the total sum and the largest element
total_sum = sum(numbers)
max_number = max(numbers)

# The sum of all elements except the maximum one
sum_without_max = total_sum - max_number

# Check if the max element is equal to the sum of the others
if max_number == sum_without_max:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    # If not equal, calculate the absolute difference
    diff = abs(max_number - sum_without_max)
    print("No")
    print(f"Diff = {diff}")
