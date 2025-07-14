import random

# Function to start the number guessing game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # User chooses the interval
    try:
        lower_bound = int(input("Enter the lower bound of the interval: "))
        upper_bound = int(input("Enter the upper bound of the interval: "))
        
        if lower_bound >= upper_bound:
            print("Invalid interval. The lower bound should be less than the upper bound.")
            return
        
        # Generate a random number within the chosen interval
        number_to_guess = random.randint(lower_bound, upper_bound)
        
        print(f"Guess a number between {lower_bound} and {upper_bound}.")
        
        # Variable to track the number of attempts
        attempts = 0
        
        while True:
            # User inputs their guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                break
    except ValueError:
        print("Please enter valid numbers for the interval and guess.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
