# Add your Python code here. E.g.
from microbit import *
import speech
import random

lengteWoordArray = 3

onderwerp = ["She", "He", "You"]
werkwoord = ["is playing", "is actually", "have"]
rest = ["hard to get", "enjoying school for the first time", "been infected with covid 19"]

def sayTheWords1(word): 
    print(word)
    speech.say(word, speed=432, pitch=432, throat=432, mouth=432)
    sleep(432)

def sayTheWords2():
    willekeurigGetal = random.randint(0, lengteWoordArray - 1)
    display.show(willekeurigGetal)
    sayTheWords1(onderwerp[willekeurigGetal])
    sayTheWords1(werkwoord[willekeurigGetal])
    sayTheWords1(rest[willekeurigGetal])

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        sayTheWords1("You scored a 10 out of 10 on your aids test")
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sayTheWords1("You have been infected with covid 19")
    elif display.read_light_level() < 40:
        sayTheWords2()
    else:
        display.show(Image.SQUARE)
        
