# Menu prices as constants
PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEG_MENU = 8.15
DELIVERY_PRICE = 2.50

# Input: number of menus for each type
num_chicken = int(input())
num_fish = int(input())
num_veg = int(input())

# Calculate total cost of the main menus
total_menu_cost = ((num_chicken * PRICE_CHICKEN_MENU)
                   + (num_fish * PRICE_FISH_MENU)
                   + (num_veg * PRICE_VEG_MENU))

# Dessert cost is 20% of the total menu cost
dessert_price = total_menu_cost * 0.20

# Final sum includes menus, dessert, and a fixed delivery fee
total_bill = total_menu_cost + dessert_price + DELIVERY_PRICE

print(total_bill)
