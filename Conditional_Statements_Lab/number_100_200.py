# Input: integer number to be categorized
number = int(input())

# Range validation logic
if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
else:
    # This block handles all numbers greater than 200
    print("Greater than 200")
