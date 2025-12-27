# Cake distribution tracking system
width = int(input())
length = int(input())

# Calculate total capacity
total_pieces = width * length
taken_pieces = 0

while True:
    command = input()
    
    if command == "STOP":
        # Calculate remaining inventory
        remaining = total_pieces - taken_pieces
        print(f"{remaining} pieces are left.")
        break

    pieces = int(command)
    taken_pieces += pieces

    # Check for inventory exhaustion
    if taken_pieces > total_pieces:
        needed = taken_pieces - total_pieces
        print(f"No more cake left! You need {needed} pieces more.")
        break
