# Input: the target number up to which the pyramid will be built
n = int(input())

current_num = 1
current_row_length = 1

# Outer loop to manage the rows of the pyramid
while current_num <= n:
    # Inner loop to print numbers on the current row
    for i in range(current_row_length):
        if current_num > n:
            break
        print(current_num, end=' ')
        current_num += 1
    
    # Move to the next line after finishing a row
    print()
    current_row_length += 1
