# Fixed exchange rate USD to BGN
USD_TO_BGN_RATE = 1.7954

# Input: amount in United States Dollars
usd_amount = float(input())

# Conversion logic
bgn_amount = usd_amount * USD_TO_BGN_RATE

# Output the result
print(bgn_amount)
