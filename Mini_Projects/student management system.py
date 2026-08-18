import json

print("="*40)
print("STUDENT MANAGEMENT SYSTEM")
print("="*40)

students = {}

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
                name = input("Student Name: ").title()
                age = int(input("Student Age: "))
                city = input("Student City: ").title()

                students[name] = {
                                  "Age": age,
                                  "City": city,
                                  "Marks": {}
                                  }

                subjects = ["Math", "Science", "Python"]
                marks = list(map(int, input("Enter three subject marks(math, science, python): ").split()))

                if len(marks) == len(subjects):
                        for subject, mark in zip(subjects, marks):
                                students[name]["Marks"][subject] = mark
                        print(students)
                                        
                else:
                        print("Marks should be 3 subjects only, try again!")

                for subject, mark in zip(subjects, marks):
                        details = {
                                "Name" : name,
                                "Age" : age,
                                "city" : city,
                                
                        }

                with open("Students Details.json", 'a') as f:
                        json.dump(students, f, indent=2)
                print("Saved in Json File")

        # view all students in dictionary
        elif choice == 2:
                for name, info in students.items():
                        print(f"{name}: {info}")

        # search the student in dictionary
        elif choice == 3:
                name = input("Enter Student Name: ").title()
                for names, info in students.items():
                        if name == names:
                                print(f"{names}: {info}")
                        else:
                                print("Name doesn't exist")


        else:
                print("Enter valid number!")

        choss = input("enter your choise(y/n): ")
        if choss == "n":
                break
        elif choss != "y":
                print("Enter only (Yes/No)")







