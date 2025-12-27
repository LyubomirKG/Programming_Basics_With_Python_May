# Algorithm for finding the minimum value in a dynamic sequence
min_num = None

while True:
    input_line = input()
    
    # Exit condition for the stream processing
    if input_line == "Stop":
        break

    current_number = int(input_line)
    
    # Initialization and comparison logic
    if min_num is None or current_number < min_num:
        min_num = current_number

# Final output check
if min_num is not None:
    print(min_num)
