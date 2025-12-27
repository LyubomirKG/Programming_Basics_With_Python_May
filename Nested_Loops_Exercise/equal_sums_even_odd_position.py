# Input: range boundaries for six-digit numbers
start = int(input())
end = int(input())

# Iterate through each number in the given range
for number in range(start, end + 1):
    number_str = str(number)

    even_sum = 0
    odd_sum = 0

    # Iterate through each digit (index 0 to 5 for a 6-digit number)
    for i in range(len(number_str)):
        digit = int(number_str[i])
        
        # Human-readable positions: 1st, 2nd, 3rd, 4th, 5th, 6th
        if (i + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    # Check if the sum of digits at even positions equals the sum at odd positions
    if even_sum == odd_sum:
        print(number, end=' ')
