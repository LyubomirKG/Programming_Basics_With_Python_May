# Input: number of groups participating in the climbing marathon
groups_count = int(input())

# Initialize group size counters for each mountain peak
musala_climbers = 0      # groups up to 5
monblan_climbers = 0     # groups 6 - 12
kilimandjaro_climbers = 0 # groups 13 - 25
k2_climbers = 0           # groups 26 - 40
everest_climbers = 0      # groups 41 or more

total_climbers = 0

# Process each group
for _ in range(groups_count):
    people_in_group = int(input())
    total_climbers += people_in_group

    if people_in_group <= 5:
        musala_climbers += people_in_group
    elif people_in_group <= 12:
        monblan_climbers += people_in_group
    elif people_in_group <= 25:
        kilimandjaro_climbers += people_in_group
    elif people_in_group <= 40:
        k2_climbers += people_in_group
    else:
        everest_climbers += people_in_group

# Calculate and display percentages relative to total climbers
print(f"{(musala_climbers / total_climbers) * 100:.2f}%")
print(f"{(monblan_climbers / total_climbers) * 100:.2f}%")
print(f"{(kilimandjaro_climbers / total_climbers) * 100:.2f}%")
print(f"{(k2_climbers / total_climbers) * 100:.2f}%")
print(f"{(everest_climbers / total_climbers) * 100:.2f}%")
