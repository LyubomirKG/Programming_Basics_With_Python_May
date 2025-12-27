# Input: Personal information
first_name = input()
last_name = input()
age = int(input())
town = input()

# Professional string interpolation using f-strings
# This format is preferred for readability and performance
print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')
