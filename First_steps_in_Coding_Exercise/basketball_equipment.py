# Input: The annual training tax for basketball
annual_training_tax = int(input())

# Calculating costs based on percentage decreases from previous items
# Sneakers are 40% cheaper than the annual tax
basketball_sneakers = annual_training_tax * 0.60

# Team outfit is 20% cheaper than the sneakers
basketball_team = basketball_sneakers * 0.80

# Ball cost is 1/4 (25%) of the outfit cost
basketball_ball = basketball_team * 0.25

# Accessories are 1/5 (20%) of the ball cost
basketball_accessories = basketball_ball * 0.20

# Summing up all expenses including the initial tax
total_sum = (annual_training_tax + basketball_sneakers + basketball_team
             + basketball_ball + basketball_accessories)

print(total_sum)
