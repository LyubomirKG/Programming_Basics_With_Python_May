def is_prime(n):
    """Checks if a number is prime using the square root optimization."""
    if n < 2:
        return False
    # Check for divisors from 2 up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_sum = 0
non_prime_sum = 0

while True:
    command = input()

    if command == "stop":
        break

    number = int(command)

    # Validate input: prime/non-prime logic only applies to non-negative integers
    if number < 0:
        print("Number is negative.")
        continue

    if is_prime(number):
        prime_sum += number
    else:
        non_prime_sum += number

# Final Report
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
