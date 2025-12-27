# Input: age (float) and gender ('m' or 'f')
age = float(input())
gender = input()

# Professional titles based on gender and age threshold
if gender == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')

elif gender == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
