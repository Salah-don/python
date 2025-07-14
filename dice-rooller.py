import random

# Function to simulate rolling a die
def roll_dice(sides):
    return random.randint(1, sides)

# Main function for the Dice Roller Simulator
def dice_roller():
    print("Welcome to the Dice Roller Simulator!")
    
    # User chooses the number of sides of the die
    try:
        sides = int(input("Enter the number of sides on the die: "))
        
        if sides < 1:
            print("A die must have at least one side. Please enter a valid number of sides.")
            return
        
        # Roll the dice as many times as the user wants
        while True:
            input("\nPress Enter to roll the dice...")
            result = roll_dice(sides)
            print(f"You rolled a {result}!")
            
            # Ask the user if they want to roll again
            roll_again = input("\nDo you want to roll again? (yes/no): ").lower()
            if roll_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break
    except ValueError:
        print("Please enter a valid number of sides.")

# Run the Dice Roller Simulator
if __name__ == "__main__":
    dice_roller()
