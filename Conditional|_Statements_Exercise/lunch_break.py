import math

# Input: series name, duration of an episode, and total break duration
series_name = input()
episode_duration = int(input())
break_duration = int(input())

# Calculating time spent on mandatory activities during the break
lunch_time = break_duration / 8
relax_time = break_duration / 4

# Remaining time available for watching the series
time_left = break_duration - lunch_time - relax_time

# Validation of available time vs. episode duration
if time_left >= episode_duration:
    # Use math.ceil to round up the remaining free time
    free_time = math.ceil(time_left - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {free_time} minutes free time.")
else:
    # Use math.ceil to round up the needed time
    needed_time = math.ceil(episode_duration - time_left)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
