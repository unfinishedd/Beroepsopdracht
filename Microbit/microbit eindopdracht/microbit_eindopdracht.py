from microbit import *
import random


display.scroll("Driehoek, Cirkel, Keer(X), Vierkant")


shapes=[Image("00900:09090:99099:99999:00000"), #Driehoek
        Image("00900:09090:90009:09090:00900"), #Cirkel
        Image("90009:09090:00900:09090:90009"), #Keer(X)
        Image("99999:90009:90009:90009:99999")] #Vierkant


while True:
    gesture = accelerometer.current_gesture() # zet de variable gesture naar de huidige gesture huidige gesture
    if gesture == "shake":                    # zorgt ervoor dat je de microbit kan schudden
        display.show(random.choice(shapes))   # laat een random shape zien
