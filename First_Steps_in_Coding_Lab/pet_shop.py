# Fixed prices for pet food packages
DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4.00

# Input: number of packages for dogs and cats
dog_packs = int(input())
cat_packs = int(input())

# Calculate total cost
total_price = (dog_packs * DOG_FOOD_PRICE) + (cat_packs * CAT_FOOD_PRICE)

# Output the result formatted with the local currency
print(f"{total_price} lv.")
