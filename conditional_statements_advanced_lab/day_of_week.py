# Position 0 is "Error" to handle 1-based indexing easily, 
# or we can just adjust the index by -1.
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Input: number representing the day of the week
day_number = int(input())

# Check if the input is within the valid range (1-7)
if 1 <= day_number <= 7:
    # Adjusting for 0-based index (1 becomes 0, 7 becomes 6)
    print(days[day_number - 1])
else:
    print("Error")
