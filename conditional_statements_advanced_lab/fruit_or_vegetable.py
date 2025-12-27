# Grouping items into categories for better maintainability
fruit_list = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetable_list = ['tomato', 'cucumber', 'pepper', 'carrot']

# Input: product name
product = input()

# Classification logic using list membership
if product in fruit_list:
    print('fruit')
elif product in vegetable_list:
    print('vegetable')
else:
    print('unknown')
