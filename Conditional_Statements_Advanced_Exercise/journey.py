# Budget limits for different destinations
BULGARIA_LIMIT = 100
BALKANS_LIMIT = 1000

budget = float(input())
season = input()

destination = ""
vacation_type = ""
spent_amount = 0

# Determine destination and costs based on budget and season
if budget <= BULGARIA_LIMIT:
    destination = "Bulgaria"
    if season == "summer":
        spent_amount = budget * 0.30
        vacation_type = "Camp"
    else:  # winter
        spent_amount = budget * 0.70
        vacation_type = "Hotel"

elif budget <= BALKANS_LIMIT:
    destination = "Balkans"
    if season == "summer":
        spent_amount = budget * 0.40
        vacation_type = "Camp"
    else:  # winter
        spent_amount = budget * 0.80
        vacation_type = "Hotel"

else:  # budget > 1000
    destination = "Europe"
    spent_amount = budget * 0.90
    vacation_type = "Hotel"

# Final output
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spent_amount:.2f}")
