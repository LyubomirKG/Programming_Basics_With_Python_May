from sys import maxsize

# Input: number of integers to process
n = int(input())

# Initialize with the largest possible system values
# max_number starts at the smallest possible, min_number at the largest
max_number = -maxsize
min_number = maxsize

for _ in range(n):
    current_number = int(input())

    # Update max if current is larger
    if current_number > max_number:
        max_number = current_number

    # Update min if current is smaller
    if current_number < min_number:
        min_number = current_number

# Professional output
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
