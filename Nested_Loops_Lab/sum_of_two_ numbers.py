# Input: range and target sum
start_range = int(input())
end_range = int(input())
magic_num = int(input())

combination_counter = 0
is_found = False

# Search through all possible pairs (x1, x2) in the given range
for x1 in range(start_range, end_range + 1):
    for x2 in range(start_range, end_range + 1):
        combination_counter += 1
        
        if x1 + x2 == magic_num:
            print(f"Combination N:{combination_counter} ({x1} + {x2} = {magic_num})")
            is_found = True
            break
            
    if is_found:
        break

# Handle the case where no such combination exists
if not is_found:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
