# Infinite echo loop with a termination command
while True:
    input_text = input()
    
    # Check for the exit signal
    if input_text == "Stop":
        break
    
    # Process or "echo" the input
    print(input_text)
