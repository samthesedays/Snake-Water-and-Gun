import random
# Definition + Logic(I)
snake = 0
water = 1
gun = 2

def check_win(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "tie"
    elif (user_choice == "0" and comp_choice == "2") or \
         (user_choice == "1" and comp_choice == "0") or \
         (user_choice == "2" and comp_choice == "1"):
        return "user"
    else:
        return "computer"

print("Welcome to Snake Water Gun!")
print("You are playing against the computer.")
print("The rules are: ")
print("Snake>Water,\nGun>Snake.\nSnake>Water")
print("snake = 0\nwater = 1\ngun = 2")

# Randomization + Logic(II)
choices = ["0", "1", "2"]

while True:
    user_choice = input("Enter your choice (0 for snake, 1 for water, or 2 for gun), or q to quit: ")
    if user_choice == "q" or user_choice == "quit":
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    comp_choice = random.choice(choices)
    print("You chose", user_choice)
    print("The computer chose", comp_choice)
    winner = check_win(user_choice, comp_choice)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Congratulations, you won!")
    else:
        print("Sorry, the computer won.")
print("Thanks for playing!")


# Debugging this code requires a runtime like Python IDE 3.12.
# Python Version : 3.12.3
