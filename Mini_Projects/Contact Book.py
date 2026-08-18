import csv
import os

print("="*40)
print("Contact Book")
print("="*40)

contacts = []

while True:
    print("  -----Menu-----")
    print(" 1. Add Contact")
    print(" 2. View all Contacts")
    print(" 3. Search Contact")
    print(" 4. Delete contact")
    print(" 5. Exit")

    try:
        user = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    if user == 1:
        name = input("Enter Name: ").title()
        phone = input("Enter Phone Number: ")
        email = input("Enter your Email: ")

        if len(phone) != 10 and phone.isdigit():
            phone = phone
        else:
            print("Enter Valid Number")

        if "@" not in email or "." not in email:
            print("Invalid")
        else:
            email = email

        details = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }

        contacts.append(details)

        file_exists = os.path.exists("Contact book.csv")

        with open("Contact book.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "phone", "email"]
            )

            if not file_exists or os.path.getsize("Contact book.csv") == 0:
                writer.writeheader()

            writer.writerows(contacts)

    elif user == 2:
        with open("Contact book.csv", 'r') as f:
            read = csv.DictReader(f)

            for contact in read:
                print(contact)

    elif user == 3:

        search = input("Enter Name: ").title()

        with open("Contact book.csv", 'r') as f:
            read = csv.DictReader(f)

            found = False

            for contact in read:
                if search == contact["name"]:
                    print(contact)
                    found = True
                    break

            if not found:
                print("Name not found!")

    elif user == 4:

        new_contacts = []

        with open("Contact book.csv", "r") as f:
            reader = csv.DictReader(f)

            for contact in reader:
                contacts.append(new_contacts)

        search = input("Enter Name: ").title()

        found = False

        for contact in read:
            if search == contact["name"]:
                contacts.remove(contact)
                found = True
                break

        if not found:
            print("Not Found")
        else:
            with open("Contact book.csv", "w", newline="") as f:
                fieldnames = ["name", "phone", "email"]

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(contacts)

    elif user == 5:
        break

    print()

    print("Want to change anything choose(yes/no)")
    choose = input("Enter your choice(y/n): ")

    if choose == "n":
        break
    elif choose != "y":
        print("Please Enter only (y/n)")
    

