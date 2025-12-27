# Change-making algorithm (Greedy approach)
amount = float(input())

# Convert total amount to cents to avoid floating-point precision issues
remaining_cents = int(round(amount * 100))

# Standard denominations from 2 units down to 1 cent
coins = [200, 100, 50, 20, 10, 5, 2, 1]
total_coins_count = 0

for coin in coins:
    if remaining_cents <= 0:
        break
    
    # Calculate how many coins of the current denomination fit
    count_of_this_coin = remaining_cents // coin
    total_coins_count += count_of_this_coin
    
    # Update the remaining balance using modulo
    remaining_cents %= coin

print(total_coins_count)
