# Daily fitness goal tracker
daily_goal = 10000
current_steps = 0

while current_steps < daily_goal:
    user_input = input()
    
    # Check if the user is finished for the day
    if user_input == "Going home":
        last_steps = int(input())
        current_steps += last_steps
        break
    
    # Otherwise, add steps to the total
    steps = int(user_input)
    current_steps += steps

# Calculate the difference between actual steps and the goal
if current_steps >= daily_goal:
    print("Goal reached! Good job!")
    print(f"{current_steps - daily_goal} steps over the goal!")
else:
    print(f"{daily_goal - current_steps} more steps to reach goal.")
