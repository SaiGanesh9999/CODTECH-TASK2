def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def get_gpa(letter_grade):
    grade_to_gpa = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_to_gpa.get(letter_grade, 0.0)

def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def main():
    print("Welcome to the Student Grade Tracker!")
    grades = []

    while True:
        subject = input("Enter the subject (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break

        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                grades.append(grade)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical grade.")

    if grades:
        average_grade = calculate_average(grades)
        letter_grade = get_letter_grade(average_grade)
        gpa = get_gpa(letter_grade)

        print("\nGrade Report")
        print("------------")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
    main()
