# Input: dimensions in centimeters and occupied volume percentage
length = int(input())
width = int(input())
height = int(input())
occupied_percent = float(input())

# Calculate total volume in cubic centimeters
volume_cm3 = length * width * height

# Convert cubic centimeters to liters (1 liter = 1000 cm3)
total_liters = volume_cm3 / 1000

# Calculate net usable volume by subtracting the occupied percentage
# (sand, filter, plants, etc.)
usable_volume = total_liters * (1 - occupied_percent / 100)

# Output the result with 3 decimal places for precision
print(f"{usable_volume:.3f}")
