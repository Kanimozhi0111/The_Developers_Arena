# Student Grade Calculator
# Project: Week 2 - Student Grade Calculator

def get_grade(marks):
    """Returns grade based on marks"""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_message(grade):
    """Returns encouraging message based on grade"""
    if grade == "A":
        return "Excellent! You're a star! 🌟"
    elif grade == "B":
        return "Very Good! Keep it up! 👍"
    elif grade == "C":
        return "Good! You can do even better! 💪"
    elif grade == "D":
        return "Fair! Need more practice! 📚"
    else:
        return "Don't give up! Try harder next time! 🎯"


def validate_marks(marks):
    """Validates if marks are between 0 and 100"""
    return 0 <= marks <= 100


def main():
    """Main program function"""
    print("=" * 40)
    print("   STUDENT GRADE CALCULATOR")
    print("=" * 40)

    # Get student name
    name = input("\nEnter student name: ")

    # Get marks with validation using while loop
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if validate_marks(marks):
                break
            else:
                print("Error: Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number. Try again.")

    # Calculate grade and message
    grade = get_grade(marks)
    message = get_message(grade)

    # Display result
    print("\n" + "=" * 40)
    print(f"📊 RESULT FOR {name.upper()}:")
    print("=" * 40)
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    main()