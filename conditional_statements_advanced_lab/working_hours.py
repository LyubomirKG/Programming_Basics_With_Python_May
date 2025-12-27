# Input: current hour and day of the week
hour = int(input())
day = input()

# Check if it's a working day (Monday to Saturday)
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    # Check if the hour is within business hours (10:00 - 18:00)
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
else:
    # Sunday or any other input results in 'closed'
    print("closed")
