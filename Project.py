# Initializing dictionary
student_grade = {}

# Add a new student
def add_student(name, grade):
    student_grade[name] = grade
    print(f"Added {name} with a {grade}")

# Update student grade
def update_student(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"{name} with marks are updated to : {grade}")
    else:
        print(f"{name} is not found")

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")

def view_student(name):
    if name in student_grade:
        print(f"{name} ---- {student_grade[name]}")
    else:
        print(f"{name} is not found")

def display_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added")

def main():
    while True:
        print('\n Student Grades managament System')
        print("1. Add student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("invalid choice. Please enter a number")
            continue

        if choice == 1:
            name = input("Enter Student name = ")
            grade = int(input("Enter Student grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter Student name = ")
            delete_student(name)

        elif choice == 4:
            name = input("Enter student name to view (optional): ")
            if name:
                view_student(name)
            else:
                display_all_students()

        elif choice == 5:
            print("Closing the program....")
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main()