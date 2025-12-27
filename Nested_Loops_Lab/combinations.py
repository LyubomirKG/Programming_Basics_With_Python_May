# Input: the sum target n
n = int(input())

combinations_count = 0

# Optimized approach: Using two loops instead of three
for x1 in range(n + 1):
    for x2 in range(n + 1):
        # Calculate x3 based on the remaining value needed to reach n
        x3 = n - x1 - x2
        
        # Check if x3 is within the valid range [0, n]
        if 0 <= x3 <= n:
            combinations_count += 1

print(combinations_count)
