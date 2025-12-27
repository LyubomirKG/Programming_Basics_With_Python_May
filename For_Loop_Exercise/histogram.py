# Input: how many numbers will be entered
n = int(input())

# Initialize counters for each range
p1 = p2 = p3 = p4 = p5 = 0

for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number <= 399:
        p2 += 1
    elif number <= 599:
        p3 += 1
    elif number <= 799:
        p4 += 1
    else:
        p5 += 1

# Calculate and display the percentage distribution for each range
# Formula: (count / total_n) * 100, formatted to 2 decimal places
print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")
