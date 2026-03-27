import random

print("🎮 Welcome to Number Guessing Game!")

# Difficulty selection
print("\nChoose Difficulty:")
print("1. Easy (1–50, 10 attempts)")
print("2. Medium (1–100, 7 attempts)")
print("3. Hard (1–200, 5 attempts)")

choice = input("Enter choice (1/2/3): ")

# Setting based on difficulty
if choice == "1":
    max_num = 50
    attempts = 10
elif choice == "2":
    max_num = 100
    attempts = 7
elif choice == "3":
    max_num = 200
    attempts = 5
else:
    print("Invalid choice! Defaulting to Easy.")
    max_num = 50
    attempts = 10

number = random.randint(1, max_num)

print(f"\nGuess a number between 1 and {max_num}")

# Game loop
for i in range(attempts):
    guess = int(input(f"Attempt {i+1}: Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You won!")
        break
    elif guess < number:
        print("Too low ⬇️")
    elif guess > number:
        print("Too high ⬆️")
    else:
        print("Invalid input")

else:
    print(f"\n😢 You lost! The number was {number}")