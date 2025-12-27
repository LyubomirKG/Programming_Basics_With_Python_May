# Student graduation tracker with failure monitoring
student_name = input()

current_grade = 1
fail_counter = 0
total_score_sum = 0

while current_grade <= 12:
    annual_score = float(input())

    # Case: Student fails the year (grade < 4.00)
    if annual_score < 4.00:
        fail_counter += 1
        # Two failures mean exclusion from the education system
        if fail_counter > 1:
            print(f"{student_name} has been excluded at {current_grade} grade")
            break
        # Skip the rest of the loop and try the same grade again
        continue

    # Case: Student passes the year
    total_score_sum += annual_score
    current_grade += 1

# If the student reaches grade 13, it means they completed grade 12
if current_grade > 12:
    final_average = total_score_sum / 12
    print(f"{student_name} graduated. Average grade: {final_average:.2f}")
