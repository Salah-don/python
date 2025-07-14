import time

# Function to start the countdown timer
def countdown_timer(seconds):
    print(f"Starting countdown from {seconds} seconds...")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(time_format, end="\r")  # Print and overwrite the same line
        time.sleep(1)
        seconds -= 1
    
    print("00:00\nTime's up!")

# Main function to take user input and start the timer
def main():
    try:
        # User enters the countdown time in seconds
        total_seconds = int(input("Enter the countdown time in seconds: "))
        
        if total_seconds <= 0:
            print("Please enter a positive number of seconds.")
        else:
            countdown_timer(total_seconds)
    
    except ValueError:
        print("Please enter a valid number for the countdown time.")

# Run the countdown timer program
if __name__ == "__main__":
    main()
