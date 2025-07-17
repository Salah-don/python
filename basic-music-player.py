import pygame
import os

def simple_music_player():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    def play_music(file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(file_path)}")
        except pygame.error as e:
            print(f"Error playing music: {e}")
    
    def stop_music():
        pygame.mixer.music.stop()
        print("Music stopped")
    
    def pause_music():
        pygame.mixer.music.pause()
        print("Music paused")
    
    def resume_music():
        pygame.mixer.music.unpause()
        print("Music resumed")
    
    # Example usage
    music_file = "your_song.mp3"  # Replace with your music file
    
    while True:
        print("\n=== Simple Music Player ===")
        print("1. Play music")
        print("2. Pause music")
        print("3. Resume music")
        print("4. Stop music")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            play_music(music_file)
        elif choice == "2":
            pause_music()
        elif choice == "3":
            resume_music()
        elif choice == "4":
            stop_music()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# Run the player
# simple_music_player()
