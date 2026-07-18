print("=== Welcome to Student Result Management System ===\n")

try:
    name = input("What is your name? ").strip().capitalize()
    student_class = input("Which class are you studying in? ").strip()
    
    maths = int(input("Marks in Maths (out of 100): "))
    science = int(input("Marks in Science (out of 100): "))
    english = int(input("Marks in English (out of 100): "))
    sst = int(input("Marks in SST (out of 100): "))
    language = int(input("Marks in Main Language (out of 100): "))

    total = maths + science + english + sst + language
    percentage = (total / 500) * 100

    print("\n" + "="*40)
    print("RESULT SUMMARY")
    print("="*40)
    print(f"Student Name : {name}")
    print(f"Class        : {student_class}")
    print(f"Total Marks  : {total}/500")
    print(f"Percentage   : {percentage:.2f}%")

    if percentage >= 90:
        print("Grade        : A (Outstanding)")
    elif percentage >= 80:
        print("Grade        : B (Excellent)")
    elif percentage >= 70:
        print("Grade        : C (Good)")
    elif percentage >= 50:
        print("Grade        : D (Pass)")
    else:
        print("Grade        : F (Fail)")

    print("="*40)

except ValueError:
    print("Error: Please enter valid numbers for marks!")
except Exception:
    print("Something went wrong. Please try again.")
