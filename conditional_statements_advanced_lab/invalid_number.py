# Input: integer number
number = int(input())

# Logical check for validity: 
# The number is valid if it's between 100 and 200 (inclusive) OR if it is 0.
# We use 'not' to print "invalid" only when these conditions are NOT met.
if not (100 <= number <= 200 or number == 0):
    print("invalid")
