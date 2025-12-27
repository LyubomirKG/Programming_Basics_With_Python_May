# Initialize global counters
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_seats = int(input())
    current_movie_tickets = 0

    # Inner loop for selling tickets per movie
    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break

        current_movie_tickets += 1
        total_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    # Calculation for current movie
    percent_full = (current_movie_tickets / free_seats) * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

# Final report across all movies
if total_tickets > 0:
    print(f"Total tickets: {total_tickets}")
    print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
    print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
    print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")
