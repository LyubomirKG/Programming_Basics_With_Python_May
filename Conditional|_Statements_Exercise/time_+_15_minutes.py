# Constant for the time jump
TIME_INCREMENT = 15

# Input: current hour and minutes
hour = int(input())
minutes = int(input()) + TIME_INCREMENT

# Handle minute overflow
if minutes >= 60:
    minutes -= 60
    hour += 1

# Handle hour overflow (24-hour clock cycle)
if hour >= 24:
    hour -= 24

# Output the time with leading zero for minutes if needed
# Using :02d is a professional way to ensure 2-digit formatting
print(f'{hour}:{minutes:02d}')
