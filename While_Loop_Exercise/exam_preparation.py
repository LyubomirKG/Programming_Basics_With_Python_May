# Exam preparation monitoring system
max_poor_grades = int(input())

poor_grades_counter = 0
total_score_sum = 0
solved_problems_count = 0
last_solved_problem = ""

while True:
    problem_name = input()
    
    # Check for the completion command
    if problem_name == "Enough":
        if solved_problems_count > 0:
            average_score = total_score_sum / solved_problems_count
            print(f"Average score: {average_score:.2f}")
            print(f"Number of problems: {solved_problems_count}")
            print(f"Last problem: {last_solved_problem}")
        break

    grade = int(input())
    total_score_sum += grade
    solved_problems_count += 1
    last_solved_problem = problem_name

    # Check for unsatisfactory grade (score <= 4)
    if grade <= 4:
        poor_grades_counter += 1
        if poor_grades_counter >= max_poor_grades:
            print(f"You need a break, {poor_grades_counter} poor grades.")
            break
