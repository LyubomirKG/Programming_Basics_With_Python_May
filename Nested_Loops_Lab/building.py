# Input: building specifications
floors_count = int(input())
rooms_per_floor = int(input())

# Traverse from the top floor down to the ground floor
for floor in range(floors_count, 0, -1):
    row_output = []
    
    for room in range(rooms_per_floor):
        # Rule 1: The top floor is always Large apartments (L)
        if floor == floors_count:
            label = f"L{floor}{room}"
        # Rule 2: Even floors are Offices (O)
        elif floor % 2 == 0:
            label = f"O{floor}{room}"
        # Rule 3: Odd floors are normal Apartments (A)
        else:
            label = f"A{floor}{room}"
        
        row_output.append(label)
    
    # Print the entire floor on a single line
    print(" ".join(row_output))
