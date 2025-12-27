# Input: string to be analyzed
text = input()

# Initialize accumulator
vowel_value_sum = 0

# Character-to-value mapping logic
for char in text:
    if char == 'a':
        vowel_value_sum += 1
    elif char == 'e':
        vowel_value_sum += 2
    elif char == 'i':
        vowel_value_sum += 3
    elif char == 'o':
        vowel_value_sum += 4
    elif char == 'u':
        vowel_value_sum += 5

# Final result
print(vowel_value_sum)
