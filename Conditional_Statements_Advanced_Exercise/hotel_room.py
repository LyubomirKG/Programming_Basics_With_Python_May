# Constants for accommodation prices per night
MAY_OCTOBER_STUDIO = 50
JUNE_SEPTEMBER_STUDIO = 75.20
JULY_AUGUST_STUDIO = 76

MAY_OCTOBER_APARTMENT = 65
JUNE_SEPTEMBER_APARTMENT = 68.70
JULY_AUGUST_APARTMENT = 77

month = input()
nights = int(input())

apartment_total = 0
studio_total = 0

# Calculate base prices and specific studio discounts based on the month
if month == 'May' or month == 'October':
    apartment_total = nights * MAY_OCTOBER_APARTMENT
    studio_total = nights * MAY_OCTOBER_STUDIO
    if nights > 14:
        studio_total *= 0.70  # 30% discount for more than 14 nights
    elif nights > 7:
        studio_total *= 0.95  # 5% discount for more than 7 nights

elif month == 'June' or month == 'September':
    apartment_total = nights * JUNE_SEPTEMBER_APARTMENT
    studio_total = nights * JUNE_SEPTEMBER_STUDIO
    if nights > 14:
        studio_total *= 0.80  # 20% discount for more than 14 nights

elif month == 'July' or month == 'August':
    apartment_total = nights * JULY_AUGUST_APARTMENT
    studio_total = nights * JULY_AUGUST_STUDIO

# Apply 10% discount for apartments if staying more than 14 nights (all months)
if nights > 14:
    apartment_total *= 0.90

# Output results formatted to 2 decimal places
print(f'Apartment: {apartment_total:.2f} lv.')
print(f'Studio: {studio_total:.2f} lv.')
