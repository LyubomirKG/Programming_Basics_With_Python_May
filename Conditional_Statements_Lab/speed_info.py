# Input: movement speed as a floating-point number
speed = float(input())

# Speed classification logic based on predefined thresholds
if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
else:
    # Handles any speed greater than 1000
    print("extremely fast")
