# Input: initial points
start_points = int(input())

bonus_points = 0

# Part 1: Calculate basic bonus points based on range
if start_points <= 100:
    bonus_points += 5
elif 100 < start_points <= 1000:
    bonus_points += (start_points * 0.20)
else:
    bonus_points += (start_points * 0.10)

# Part 2: Additional points based on number properties
if start_points % 2 == 0:
    # Bonus for even numbers
    bonus_points += 1
elif start_points % 10 == 5:
    # Bonus for numbers ending in 5
    bonus_points += 2

# Output the calculated bonus and the total score
print(bonus_points)
print(bonus_points + start_points)
