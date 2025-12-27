# 3D Warehouse/Moving space optimization system
width = int(input())
length = int(input())
height = int(input())

# Total volume in cubic meters
total_volume = width * length * height
current_used_volume = 0

while True:
    command = input()
    
    # Check for manual completion
    if command == "Done":
        remaining_space = total_volume - current_used_volume
        print(f"{remaining_space} Cubic meters left.")
        break

    # Process incoming boxes
    incoming_boxes = int(command)
    current_used_volume += incoming_boxes

    # Trigger alert if volume is exceeded
    if current_used_volume > total_volume:
        needed_space = current_used_volume - total_volume
        print(f"No more free space! You need {needed_space} Cubic meters more.")
        break
