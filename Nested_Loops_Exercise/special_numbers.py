# Input: integer n to check for divisibility
n = int(input())

# Iterate through all four-digit numbers
for number in range(1111, 10000):
    is_special = True
    number_as_str = str(number)
    
    # Check each digit of the current number
    for digit_char in number_as_str:
        digit = int(digit_char)
        
        # A number is not special if it contains 0 
        # or if n is not divisible by the digit
        if digit == 0 or n % digit != 0:
            is_special = False
            break
            
    # If all digits passed the test, print the number
    if is_special:
        print(number, end=" ")
