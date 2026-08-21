import csv
import os

print("="*40)
print("STUDENT MANAGEMENT SYSTEM")
print("="*40)

students = []

while True:
    print()
    print("----Menu----")
    print(" 1. Add Student")
    print(" 2. View All Student")
    print(" 3. Search Student")
    print(" 4. Delete Student")
    print(" 5. Analytic Dashboard")
    print(" 6. Grade Report")
    print(" 7. Export Summary")
    print(" 8. Exit")
    print()

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Enter Valid Numbers!")

        # Add Student in dictionary
    if choice == 1:
        print("Add Student Details....")
        print()

        name = input("Student Name: ").title()
        age = int(input("Student Age: "))
        city = input("Student City: ").title()
        math = int(input("Enter Math Marks: "))
        science = int(input("Enter Science Marks: "))
        python = int(input("Enter Python Marks: "))

        student = {
                "Name" : name,
                "Age"  : age,
                "Math" : math,
                "Science" : science,
                "Python" : python,
                "City" : city
            }
        students.append(student)

        file_exists = os.path.exists("Student Management.csv")

        with open("Student Management.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Math", "Science", "Python", "City"])

            if not file_exists or os.path.getsize("Student Management.csv") == 0:
                writer.writeheader()

            writer.writerows(students)
                

        # view all students in dictionary
    elif choice == 2:
        with open("Student Management.csv", "r") as file:
            reader = csv.DictReader(file)

            for read in reader:
                print(read)

        # search the student in dictionary
    elif choice == 3:
        search = input("Enter Name: ").title()

        with open("Student Management.csv", "r") as file:
            reader = csv.DictReader(file)

            for student in reader:
                if search == student["Name"]:
                    print(student)
                    break
                else:
                    print("Name not Found!")

    elif choice == 4:

        students = []

        search = input("Enter Name: ").title()

        with open("Student Management.csv", "r") as file:
            reader = csv.DictReader(file)

            for student in reader:
                students.append(student)

            found = False

            for student in reader:
                if search == student["Name"]:
                    students.remove(student)
                    found = True
                    break

            if not found:
                print("Name not Found!...")
            else:
                with open("Student Management.csv", "w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Math", "Science", "Python", "City"])

                    writer.writeheader()
                    writer.writerow(students)

                print("Succefully Deleted!")
        

    chosse = input("enter your choise(y/n): ")
    if chosse == "n":
        break
    elif chosse != "y":
        print("Enter only (Yes/No)")







