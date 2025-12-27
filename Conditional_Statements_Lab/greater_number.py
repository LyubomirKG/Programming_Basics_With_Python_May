# Input: two integer numbers
first_number = int(input())
second_number = int(input())

# Determine and print the larger number
if first_number > second_number:
    print(first_number)
else:
    # This covers cases where second_number is greater OR both are equal
    print(second_number)
