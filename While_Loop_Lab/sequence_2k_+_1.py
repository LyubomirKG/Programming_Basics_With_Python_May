# Generates a sequence where each number is 2n + 1
limit = int(input())
current_num = 1

while current_num <= limit:
    print(current_num)
    # The core logic: double the current value and add one
    current_num = 2 * current_num + 1
