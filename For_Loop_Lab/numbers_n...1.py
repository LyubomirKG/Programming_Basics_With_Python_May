# Input: starting number for the countdown
n = int(input())

# Countdown loop from n down to 1
# range(start, stop, step)
for number in range(n, 0, -1):
    print(number)
