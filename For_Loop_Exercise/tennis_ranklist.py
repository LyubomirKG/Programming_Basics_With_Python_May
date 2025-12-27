import math

# Input: number of tournaments and starting points in the ranklist
tournaments_count = int(input())
initial_points = int(input())

points_from_games = 0
wins_count = 0

# Processing each tournament result
for _ in range(tournaments_count):
    stage_reached = input() # W, F, or SF
    
    if stage_reached == "W":
        points_from_games += 2000
        wins_count += 1
    elif stage_reached == "F":
        points_from_games += 1200
    elif stage_reached == "SF":
        points_from_games += 720

# Final ranklist points
final_points = initial_points + points_from_games

# Average points per tournament (rounded down to the nearest integer)
average_points = math.floor(points_from_games / tournaments_count)

# Win rate percentage
win_rate = (wins_count / tournaments_count) * 100

# Professional Output
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_rate:.2f}%")
