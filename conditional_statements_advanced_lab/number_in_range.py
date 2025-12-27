# Input: integer number
number = int(input())

# Check if the number is within the range [-100, 100] and is not zero
if -100 <= number <= 100 and number != 0:
    print('Yes')
else:
    print('No')
