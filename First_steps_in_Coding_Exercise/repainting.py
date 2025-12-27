# Unit prices for materials
NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5
BAGS_PRICE = 0.40

# Input: quantities and labor hours
qty_nylon = int(input())
qty_paint = int(input())
qty_thinner = int(input())
hours = int(input())

# Add buffers as per requirements
# 2 sq.m. extra nylon and 10% extra paint
total_nylon = qty_nylon + 2
total_paint = qty_paint * 1.10

# Calculate total materials cost
sum_materials = ((total_nylon * NYLON_PRICE)
                 + (total_paint * PAINT_PRICE)
                 + (qty_thinner * THINNER_PRICE)
                 + BAGS_PRICE)

# Labor cost: 30% of total materials cost per hour
labor_rate_per_hour = sum_materials * 0.30
total_labor_cost = labor_rate_per_hour * hours

# Final total
total_sum = sum_materials + total_labor_cost

print(total_sum)
