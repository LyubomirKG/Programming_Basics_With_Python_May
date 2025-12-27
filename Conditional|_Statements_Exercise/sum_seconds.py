# Input: three race times in seconds
first_time = int(input())
second_time = int(input())
third_time = int(input())

# Calculate total duration
total_time = first_time + second_time + third_time

# Convert to minutes and seconds
minutes = total_time // 60
seconds = total_time % 60

# Format output to ensure leading zero for seconds less than 10
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
