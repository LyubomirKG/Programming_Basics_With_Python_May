# Input: total pages, reading speed (pages per hour), and deadline (days)
total_pages = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())

# Step 1: Calculate total hours needed to read the whole book
total_hours_needed = total_pages // pages_per_hour

# Step 2: Divide total hours by the number of days to get daily workload
hours_per_day = total_hours_needed // days_to_finish

# Output the result
print(hours_per_day)
