# Reading the day of the week from the user
# Using .capitalize() ensures the input matches our list format (e.g., "monday" becomes "Monday")
day = input().capitalize()

# Lists of working days and weekend days
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

# Validation and result output
if day in working_days:
    print("Working day")
elif day in weekend_days:
    print("Weekend")
else:
    # Handles cases where the input is not a valid day of the week
    print("Error")
