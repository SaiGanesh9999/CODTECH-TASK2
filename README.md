**Name:-** DEVARASETTI SAI GANESH 

**Comapny:-** CODTECH IT SOLUTIONS 

**ID:-** CT08DS6352 

**Domain:-** PYTHON PROGRAMMING 

**Duration:-** AUGUST 1st, 2024 to SEPTEMBER 1st, 2024 

**Mentor:-**  Muzammil Ahmed

## Overview
The Student Grade Tracker is a Python-based console application designed to help students track their grades. It allows users to input grades for different subjects, calculates the average grade, determines the corresponding letter grade, and computes the Grade Point Average (GPA). This application is user-friendly and provides a simple way for students to keep track of their academic performance.

## Key Activities
User Input: The program prompts users to input their grades for various subjects until they choose to stop by typing 'done'.
Grade Calculation: The program calculates the average of the entered grades.
Letter Grade Assignment: Based on the average grade, a letter grade is assigned according to a predefined grading scale.
GPA Calculation: The program converts the letter grade to a GPA using a mapping dictionary.
Output: The final average grade, letter grade, and GPA are displayed to the user.

## Key Insights
The program is designed with a user-centric approach, ensuring easy input and error handling.
It employs a simple yet effective method to map numerical grades to letter grades and subsequently to GPA values.
The modular design of the functions (for calculating average, determining letter grade, and computing GPA) enhances readability and maintainability.

## Technologies Used
Python: The primary programming language used to implement the logic of the grade tracker.
Console Input/Output: Utilized for interacting with the user to receive input and display results.
Data Structures: Lists and dictionaries are used to store grades and map letter grades to GPA values.

## Code 
**Code:- **
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

## Summary
The Student Grade Tracker is a straightforward application that assists students in monitoring their academic progress by providing a detailed grade report. By allowing users to input their grades, it calculates the average grade, assigns a corresponding letter grade, and computes the GPA, all while ensuring a smooth user experience through error handling and clear instructions.
