import time
import os

#uitleg
vers1 = "ik heb 3 vragen om aan u te stellen"
vraag1= "hoe oud ben ik? "
vraag2= "waar woon ik?"
vraag3= "wat is mijn mijn favoriete artiest?"
kies= "kies tussen A, B, C. "
brk= "______________________________________________________________________"
F= "dit antwoord is fout!"
T="dit antwoord is goed!"
N="voer een antwoord in."
O="Wil je nog een keer proberen? Beantwoord met Y/N."

#voorstellen
print ("hello you, ik ben Sam.")

#naam vragen
naam = input("wat is jouw voornaam? ")


print ("hallo "+ naam)

time.sleep (1)

print(vers1)

time.sleep (1)
print(brk)

#vraag1
print(vraag1)

#keuzes
print("A = 15")
print("B = 17")
print("C = 19")

X= input(kies)

if ( X == "C" ) :
    print(T)
else:
    print(F)

print(brk)

time.sleep (1)

#vraag2
print(vraag2)

#keuzes
print("A = Amstelveen")
print("B = Hoofddorp")
print("C = Amsterdam")

Z= input(kies)

if ( Z == "B" ) :
    print(T)
else:
    print(F)

print(brk)

time.sleep (1)

#vraag3
print(vraag3)

#keuzes
print("A = Juice WRLD")
print("B = XXXTENTACION")
print("C = Drake")

C= input(kies)

if ( C == "B" ) :
    print(T)
else:
    print(F)

retry = input("wil je dit nog een keer proberen? Y/N ")

print(brk)

if (retry == "Y"):
    os.system('python "ditbenik.py"')
else:
    print("gemaakt door Sam.")
