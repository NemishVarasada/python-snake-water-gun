import random

# Define choices
choices = {"s": 1, "w": -1, "g": 0}

# Computer's random choice
computer = random.choice([-1, 0, 1])

# Input from user
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if youstr not in choices:
    print("Invalid input!")
else:
    you = choices[youstr]

    # Draw condition
    if computer == you:
        print("It's a draw!")

    # Win/Lose conditions
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")

    # Display choices
    print(f"Computer chose: {['water', 'gun', 'snake'][computer + 1]}")
