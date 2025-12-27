# Constants for resistance calculation
WATER_RESISTANCE_DISTANCE = 15
WATER_RESISTANCE_DELAY = 12.5

# Input: Current world record, distance, and swimmer's speed
record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

# Calculate delays caused by water resistance
# Every 15 meters adds 12.5 seconds of delay
delay_count = distance_in_meters // WATER_RESISTANCE_DISTANCE
total_delay = delay_count * WATER_RESISTANCE_DELAY

# Total swimming time calculation
total_swimming_time = (distance_in_meters * time_per_meter) + total_delay

# Output the result based on whether the record was broken
if total_swimming_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_swimming_time:.2f} seconds.')
else:
    time_difference = total_swimming_time - record_in_seconds
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')
