# Input: exam start time and arrival time
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

# Convert everything to total minutes from start of the day
exam_total_minutes = exam_hour * 60 + exam_minute
arrival_total_minutes = arrival_hour * 60 + arrival_minute

# Calculate the difference in minutes
diff = arrival_total_minutes - exam_total_minutes

# Determine arrival status and output the time difference
if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
else:
    hours = diff // 60
    minutes = diff % 60
    print(f"{hours}:{minutes:02d} hours after the start")

elif diff == 0 or abs(diff) <= 30:
    print("On time")
    if diff != 0:
        print(f"{abs(diff)} minutes before the start")

else:  # diff < -30
    print("Early")
    if abs(diff) < 60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hours = abs(diff) // 60
        minutes = abs(diff) % 60
        print(f"{hours}:{minutes:02d} hours before the start")
