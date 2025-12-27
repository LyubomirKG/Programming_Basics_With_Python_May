# Constants: Time required per single project in hours
HOURS_PER_PROJECT = 3

# Input: Architect's name and total number of projects
name_of_architect = input()
number_of_projects = int(input())

# Calculate total hours needed
total_hours_needed = number_of_projects * HOURS_PER_PROJECT

# Output the summary using formatted string
print(f'The architect {name_of_architect} will need {total_hours_needed} '
      f'hours to complete {number_of_projects} project/s.')
