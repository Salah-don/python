import random

def word_guessing_game():
    # List of words to guess from
    words = ['rainbow', 'computer', 'science', 'programming', 'python', 
             'mathematics', 'player', 'condition', 'reverse', 'water', 
             'board', 'geeks', 'challenge', 'adventure', 'mystery']
    
    # Get player's name
    name = input("What is your name? ")
    print(f"Good Luck, {name}!")
    
    # Choose a random word
    word = random.choice(words)
    print("Guess the characters")
    
    # Initialize game variables
    guesses = ''
    turns = 12
    
    # Main game loop
    while turns > 0:
        failed = 0
        
        # Display current progress
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        
        # Check if player won
        if failed == 0:
            print("\nYou Win! 🎉")
            print(f"The word is: {word}")
            break
        
        print()  # New line
        
        # Get player's guess
        guess = input("Guess a character: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        # Check if already guessed
        if guess in guesses:
            print("You already guessed that letter!")
            continue
        
        # Add guess to guesses string
        guesses += guess
        
        # Check if guess is wrong
        if guess not in word:
            turns -= 1
            print("Wrong!")
            print(f"You have {turns} more guesses")
            
            if turns == 0:
                print("You Lose! 😞")
                print(f"The word was: {word}")
        else:
            print("Good guess!")

# Enhanced version with more features
def enhanced_word_game():
    words = {
        'easy': ['cat', 'dog', 'sun', 'car', 'hat'],
        'medium': ['python', 'coding', 'games', 'music', 'books'],
        'hard': ['programming', 'algorithm', 'development', 'technology']
    }
    
    print("=== Enhanced Word Guessing Game ===")
    name = input("Enter your name: ")
    
    # Choose difficulty
    print("\nChoose difficulty:")
    print("1. Easy (3-4 letters)")
    print("2. Medium (5-6 letters)")
    print("3. Hard (7+ letters)")
    
    while True:
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                difficulty = 'easy'
                turns = 8
            elif choice == 2:
                difficulty = 'medium'
                turns = 10
            elif choice == 3:
                difficulty = 'hard'
                turns = 12
            else:
                print("Please enter 1, 2, or 3")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    
    word = random.choice(words[difficulty])
    guesses = set()
    wrong_guesses = set()
    
    print(f"\nHello {name}! You chose {difficulty} difficulty.")
    print(f"The word has {len(word)} letters.")
    print(f"You have {turns} attempts.")
    print("Let's start!\n")
    
    while turns > 0:
        # Display current state
        display = ""
        for char in word:
            if char in guesses:
                display += char + " "
            else:
                display += "_ "
        
        print(f"Word: {display}")
        print(f"Wrong letters: {', '.join(sorted(wrong_guesses))}")
        print(f"Remaining turns: {turns}")
        
        # Check win condition
        if all(char in guesses for char in word):
            print(f"\n🎉 Congratulations {name}! You guessed '{word}' correctly!")
            print(f"You won with {turns} turns remaining!")
            break
        
        # Get guess
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guesses or guess in wrong_guesses:
            print("You already tried that letter!")
            continue
        
        # Process guess
        if guess in word:
            guesses.add(guess)
            print(f"✓ Good guess! '{guess}' is in the word!")
        else:
            wrong_guesses.add(guess)
            turns -= 1
            print(f"✗ Sorry, '{guess}' is not in the word.")
        
        print("-" * 40)
    
    if turns == 0:
        print(f"\n😞 Game Over! The word was '{word}'")
        print("Better luck next time!")

# Simple version to run
if __name__ == "__main__":
    print("Choose game version:")
    print("1. Simple version")
    print("2. Enhanced version")
    
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "2":
        enhanced_word_game()
    else:
        word_guessing_game()
