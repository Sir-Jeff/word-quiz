def get_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 60 and score < 70:
        return 'D'
    elif score >= 0 and score < 60:
        return 'E'
    else:
        return 'Invalid score'

# Example usage
score = float(input("Enter the score: "))
grade = get_grade(score)
print(f"The grade for a score of {score} is: {grade}")
