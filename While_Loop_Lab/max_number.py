# Algorithm for finding the maximum value in a dynamic sequence
max_num = None

while True:
    input_line = input()
    
    # Exit condition
    if input_line == "Stop":
        break

    current_number = int(input_line)
    
    # Check if this is the first number or a new maximum
    if max_num is None or current_number > max_num:
        max_num = current_number

# Display the result
if max_num is not None:
    print(max_num)
