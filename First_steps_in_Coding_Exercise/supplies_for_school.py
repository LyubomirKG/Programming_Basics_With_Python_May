# Unit prices for school materials
PRICE_PACKAGES_PENS = 5.80
PRICE_PACKAGES_MARKERS = 7.20
PRICE_CLEANING_PREP = 1.20

# Input: quantities and discount percentage
number_packages_pens = int(input())
number_packages_markers = int(input())
liters_cleaning_prep = int(input())
# Converting discount from integer to decimal (e.g., 25 becomes 0.25)
discount_factor = int(input()) / 100

# Step 1: Calculate total sum before discount
total_before_discount = ((number_packages_pens * PRICE_PACKAGES_PENS)
                         + (number_packages_markers * PRICE_PACKAGES_MARKERS)
                         + (liters_cleaning_prep * PRICE_CLEANING_PREP))

# Step 2: Apply the discount percentage
final_price = total_before_discount * (1 - discount_factor)

print(final_price)
