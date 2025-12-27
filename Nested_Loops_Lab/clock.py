# Generates a 24-hour clock display using nested loops
# The outer loop handles the hours (0-23)
for hour in range(24):
    # The inner loop handles the minutes (0-59) for each hour
    for minute in range(60):
        # Professional display format
        print(f"{hour}:{minute}")
