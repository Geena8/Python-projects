# import random module to help with dice roll
import random

# Set start of game to True
start_game = True

# Set a While true
while start_game is True:
    # ask for user input to the question "Roll the dice?(y/n)"
    user_input = input("Roll the dice? (y/n)")
    # Use randint to return an integer between a range in the brackets
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    # check if the input is valid (y, n, Y, N)
    # to make all inputs lowercases use the .lower() method (DON'T FORGET THE BRACKETS)
    if user_input.lower() == "y":
        print(f"({dice_1}, {dice_2})")
    elif user_input.lower() == "n":
        # To brerak out of while loops, one can use the "break" keyword or set the original True value to False 
        start_game = False
        # Return False can't be used outside of a function
        # return False - This can't be used in a while loop.
    else:
        print("Invalid choice")

# if valid print two random numbers on the screen.
