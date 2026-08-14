import random

print("="*40)
print("Welcome To Number Guessing Game")
print("="*40)

while True:

    number = random.randint(1, 100)
    count = 0

    while True:
        user_guess = int(input("Enter Number b/w (1-100): "))
        count += 1

        if user_guess > number:
            print("too high")
        elif user_guess < number:
            print("too low")
        else:
            print("correct")
            print(f"You completed in {count} attempts")
            break

    choice = input("Play Again(y/n): ").lower()
    print()
    if choice == "n":
        break
    elif choice != "y":
        print("choose only (y/n)")
