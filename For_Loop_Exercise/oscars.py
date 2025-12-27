# Constants
NOMINATION_THRESHOLD = 1250.5

# Input: Actor's initial data
actor_name = input()
total_points = float(input())
jury_count = int(input())

# Processing jury evaluations
for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())

    # Calculate points based on name length and jury's score
    added_points = (len(jury_name) * jury_points) / 2
    total_points += added_points

    # Early exit if threshold is reached
    if total_points > NOMINATION_THRESHOLD:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    # This executes only if the loop finishes without a 'break'
    needed = NOMINATION_THRESHOLD - total_points
    print(f"Sorry, {actor_name} you need {needed:.1f} more!")
