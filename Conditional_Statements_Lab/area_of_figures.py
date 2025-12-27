from math import pi

# Input: type of geometric figure
figure_type = input()
area = 0

# Area calculation based on figure geometry
if figure_type == 'square':
    side = float(input())
    area = side * side

elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b

elif figure_type == 'circle':
    radius = float(input())
    # Using math.pi for high precision calculations
    area = pi * (radius ** 2)

elif figure_type == 'triangle':
    base = float(input())
    height = float(input())
    # Formula for triangle area: (base * height) / 2
    area = (base * height) / 2

# Output the result formatted to 3 decimal places
print(f'{area:.3f}')
