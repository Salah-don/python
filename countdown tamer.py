import time  # Module pour gérer le temps

def countdown_timer(seconds):
    for i in range(seconds,0, -1): 
        print(i)
        time.sleep(1)  # Pause de 1 seconde
    print("Décollage ! 🚀")

# Appel de la fonction avec 10 secondes
countdown_timer(10)
