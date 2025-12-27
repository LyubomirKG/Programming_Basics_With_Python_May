# Input: number of jury members
jury_count = int(input())

total_average_scores_sum = 0
presentations_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    current_presentation_sum = 0
    # Collect scores from each jury member
    for _ in range(jury_count):
        score = float(input())
        current_presentation_sum += score

    # Calculate average for the current presentation
    current_average = current_presentation_sum / jury_count
    total_average_scores_sum += current_average
    presentations_count += 1

    print(f"{presentation_name} - {current_average:.2f}.")

# Calculate and print the final overall assessment
final_assessment = total_average_scores_sum / presentations_count
print(f"Student's final assessment is {final_assessment:.2f}.")
