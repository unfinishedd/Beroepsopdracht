<<<<<<< HEAD
import time

x = 0

print('Hello You! ik ben Sam.')
time.sleep(1)

print("Wie ben jij?")
naam = input()
time.sleep(1)

print("Hallo " + naam + ", kan je wel raden hoe oud ik ben? waarschijnlijk niet maar alsnog succes!")
print("a). 17")
print("b). 19")
print("c). 21")
time.sleep(1)

antwoord_1 = input()
if antwoord_1.lower() == "b" or antwoord_1.lower() == "19":
  time.sleep(1)
  print("Dat is goed, volgende vraag!")
  x = x + 1
elif antwoord_1.lower() == "a" or antwoord_1.lower() == "17":
  time.sleep(1)
  print("Dat is net niet goed, iets hoger. Ik ben namelijk 19, volgende vraag!")
elif antwoord_1.lower() == "c" or antwoord_1.lower() == "21":
  time.sleep(1)
  print("Dat is net niet goed, iets lager. Ik ben namelijk 19, volgende vraag!")
else:
  time.sleep(1)
  print("Is het correct antwoorden van een vraag zo moeilijk? Laat maar, volgende vraag.")
time.sleep(2)

print("Oké " + naam + ", waar denk je dat ik woon?")
print("a). Amsterdam")
print("b). Schiphol")
print("c). Hoofddorp")
time.sleep(1)


split = 0


while split < 1:
  antwoord_2 = input()
  if antwoord_2.lower() == "a" or antwoord_2.lower() == "Amsterdam":
    time.sleep(1)
    split = split + 1
    print("Dat is niet correct ik woon in hoofddorp, maar ik zou deze stad wel als een tweede thuis zien.")
    time.sleep(1)
  elif antwoord_2.lower() == "b" or antwoord_2.lower() == "Schiphol":
    time.sleep(1)
    print("Waarom zou iemand op Schiphol willen wonen. Ik had beter van je verwacht. Ik woon in Hoofddorp maar Amsterdam is mijn 2e thuis")
  elif antwoord_2.lower() == "c" or antwoord_2.lower() == "Hoofddorp":
    time.sleep(1)
    print("Dat is helemaal correct, Hoofddorp is geweldig en Amsterdam is zeker weten mijn 2e thuis. volgende vraag!")
    x = x + 1
    split = split + 2
  else:
    time.sleep(1)
    print("Uhhm... probeer maar opnieuw, als je het wel aan kan.")
time.sleep(2)



if split == 1:
  print("Waar in amsterdam denk je dat ik mijn thuis zou noemen?")
  print("a). Amsterdam Zuid")
  print("b). Amsterdam West")
  print("c). Amsterdam Centrum")
  time.sleep(1)

  antwoord_4 = input()
  if antwoord_4.lower() == "a" or antwoord_4.lower() == "Amsterdam Zuid":
    time.sleep(1)
    print("Dat is goed, Punt erbij!")
    x = x + 1
  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "Amsterdam west":
    time.sleep(1)
    print("Dat is niet goed, ik vind Amsterdam zuid iets beter maar west komt wel dichtbij")
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "Amsterdam Centrum":
    time.sleep(1)
    print("Dat is niet goed, ik vind Amsterdam zuid iets beter sinds ik daar vorig jaar op school zat en daar de buurt ook al goed ken.")
  else:
    time.sleep(1)
    print("Nou, uhhm oke interresant... ")
    time.sleep(3)
    print("Oke, anders...")
  time.sleep(2)


  
if split == 2:
  print("Een na laatste vraag " + naam + ", welke van deze 3 opties is een hobby van mij?")
  print("a). Het universum beter leren kennen")
  print("b). Gamen met vrienden")
  print("c). Buiten voetballen")
  time.sleep(1)

 
  
  antwoord_3 = input()
  if antwoord_3.lower() == "a" or antwoord_3.lower() == "Het universum beter leren kennen":
    time.sleep(1)
    print("Dit is mijn favortiete sinds ik elke dag nieuwe dingen erover leer, ze waren trouwens alle 3 goed!")
    x = x + 1
  elif antwoord_3.lower() == "b" or antwoord_3.lower() == "Gamen met vrienden":
    time.sleep(1)
    print("Dit doe ik wel vaak en het is een goeie manier van tijd verspillen wanneer je niks beters te doen hebt trouwens ze waren trouwens alle 3 goed!")
    x = x + 1
  elif antwoord_3.lower() == "c" or antwoord_3.lower() == "Buiten voetballen":
    time.sleep(1)
    print("Dat is goed! Ik hou echt veel van voetbal en ben er ook altijd goed in geweest trouwens ze waren alle 3 goed!")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm ben je er klaar voor?... ")
    time.sleep(3)
    print("Doe je eigen ding maar...")
  time.sleep(2)


else:
  print("Laatste vraag " + naam + ", welke van deze 3 opties is mijn favoriete voetbalteam? Neem je tijd")
  print("a). FC Bayern Munchen ")
  print("b). Real Madrid ")
  print("c). FC Barcelona")
  time.sleep(1)

 
  
  antwoord_4 = input()
  if antwoord_3.lower() == "a" or antwoord_4.lower() == "FC Bayern Munchen":
    time.sleep(1)
    print("Ik vond ze wel een redelijke club todat ze Barcelona hadden mishandeld!")

  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "Real Madrid":
    time.sleep(1)
    print("Oke... succes met je toekomst!")
    
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "FC Barcelona":
    time.sleep(1)
    print("Dat is helemaal correct! Ik hou echt veel van Barcelona niet alleen als club maar ook als stad hoe ze anders zijn en alles ik was 1,5 jaar geleden daar ook op vakantie geweest!")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm het de laatste vraag kom op?... ")
    time.sleep(3)
    print("Doe je eigen ding maar, mij boeit het niet meer...")
  time.sleep(2)

if x == 4:
  print("Je had alles goed, volgende keer beter.")
else:
  print("Je had niet alles goed! Goed gedaan!")
  

time.sleep(3)
=======
import time

x = 0

print('Hello You! ik ben Sam.')
time.sleep(1)

print("Wie ben jij?")
naam = input()
time.sleep(1)

print("Hallo " + naam + ", kan je wel raden hoe oud ik ben? waarschijnlijk niet maar alsnog succes!")
print("a). 17")
print("b). 19")
print("c). 21")
time.sleep(1)

antwoord_1 = input()
if antwoord_1.lower() == "b" or antwoord_1.lower() == "19":
  time.sleep(1)
  print("Dat is goed, volgende vraag!")
  x = x + 1
elif antwoord_1.lower() == "a" or antwoord_1.lower() == "17":
  time.sleep(1)
  print("Dat is net niet goed, iets hoger. Ik ben namelijk 19, volgende vraag!")
elif antwoord_1.lower() == "c" or antwoord_1.lower() == "21":
  time.sleep(1)
  print("Dat is net niet goed, iets lager. Ik ben namelijk 19, volgende vraag!")
else:
  time.sleep(1)
  print("Is het correct antwoorden van een vraag zo moeilijk? Laat maar, volgende vraag.")
time.sleep(2)

print("Oké " + naam + ", waar denk je dat ik woon?")
print("a). Amsterdam")
print("b). Schiphol")
print("c). Hoofddorp")
time.sleep(1)


split = 0


while split < 1:
  antwoord_2 = input()
  if antwoord_2.lower() == "a" or antwoord_2.lower() == "Amsterdam":
    time.sleep(1)
    split = split + 1
    print("Dat is niet correct ik woon in hoofddorp, maar ik zou deze stad wel als een tweede thuis zien.")
    time.sleep(1)
  elif antwoord_2.lower() == "b" or antwoord_2.lower() == "Schiphol":
    time.sleep(1)
    print("Waarom zou iemand op Schiphol willen wonen. Ik had beter van je verwacht. Ik woon in Hoofddorp maar Amsterdam is mijn 2e thuis")
  elif antwoord_2.lower() == "c" or antwoord_2.lower() == "Hoofddorp":
    time.sleep(1)
    print("Dat is helemaal correct, Hoofddorp is geweldig en Amsterdam is zeker weten mijn 2e thuis. volgende vraag!")
    x = x + 1
    split = split + 2
  else:
    time.sleep(1)
    print("Uhhm... probeer maar opnieuw, als je het wel aan kan.")
time.sleep(2)



if split == 1:
  print("Waar in amsterdam denk je dat ik mijn thuis zou noemen?")
  print("a). Amsterdam Zuid")
  print("b). Amsterdam West")
  print("c). Amsterdam Centrum")
  time.sleep(1)

  antwoord_4 = input()
  if antwoord_4.lower() == "a" or antwoord_4.lower() == "Amsterdam Zuid":
    time.sleep(1)
    print("Dat is goed, Punt erbij!")
    x = x + 1
  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "Amsterdam west":
    time.sleep(1)
    print("Dat is niet goed, ik vind Amsterdam zuid iets beter maar west komt wel dichtbij")
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "Amsterdam Centrum":
    time.sleep(1)
    print("Dat is niet goed, ik vind Amsterdam zuid iets beter sinds ik daar vorig jaar op school zat en daar de buurt ook al goed ken.")
  else:
    time.sleep(1)
    print("Nou, uhhm oke interresant... ")
    time.sleep(3)
    print("Oke, anders...")
  time.sleep(2)


  
if split == 2:
  print("Een na laatste vraag " + naam + ", welke van deze 3 opties is een hobby van mij?")
  print("a). Het universum beter leren kennen")
  print("b). Gamen met vrienden")
  print("c). Buiten voetballen")
  time.sleep(1)

 
  
  antwoord_3 = input()
  if antwoord_3.lower() == "a" or antwoord_3.lower() == "Het universum beter leren kennen":
    time.sleep(1)
    print("Dit is mijn favortiete sinds ik elke dag nieuwe dingen erover leer, ze waren trouwens alle 3 goed!")
    x = x + 1
  elif antwoord_3.lower() == "b" or antwoord_3.lower() == "Gamen met vrienden":
    time.sleep(1)
    print("Dit doe ik wel vaak en het is een goeie manier van tijd verspillen wanneer je niks beters te doen hebt trouwens ze waren trouwens alle 3 goed!")
    x = x + 1
  elif antwoord_3.lower() == "c" or antwoord_3.lower() == "Buiten voetballen":
    time.sleep(1)
    print("Dat is goed! Ik hou echt veel van voetbal en ben er ook altijd goed in geweest trouwens ze waren alle 3 goed!")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm ben je er klaar voor?... ")
    time.sleep(3)
    print("Doe je eigen ding maar...")
  time.sleep(2)


else:
  print("Laatste vraag " + naam + ", welke van deze 3 opties is mijn favoriete voetbalteam? Neem je tijd")
  print("a). FC Bayern Munchen ")
  print("b). Real Madrid ")
  print("c). FC Barcelona")
  time.sleep(1)

 
  
  antwoord_4 = input()
  if antwoord_3.lower() == "a" or antwoord_4.lower() == "FC Bayern Munchen":
    time.sleep(1)
    print("Ik vond ze wel een redelijke club todat ze Barcelona hadden mishandeld!")

  elif antwoord_4.lower() == "b" or antwoord_4.lower() == "Real Madrid":
    time.sleep(1)
    print("Oke... succes met je toekomst!")
    
  elif antwoord_4.lower() == "c" or antwoord_4.lower() == "FC Barcelona":
    time.sleep(1)
    print("Dat is helemaal correct! Ik hou echt veel van Barcelona niet alleen als club maar ook als stad hoe ze anders zijn en alles ik was 1,5 jaar geleden daar ook op vakantie geweest!")
    x = x + 1
  else:
    time.sleep(1)
    print("Nou, uhhm het de laatste vraag kom op?... ")
    time.sleep(3)
    print("Doe je eigen ding maar, mij boeit het niet meer...")
  time.sleep(2)

if x == 4:
  print("Je had alles goed, volgende keer beter.")
else:
  print("Je had niet alles goed! Goed gedaan!")
  

time.sleep(3)
>>>>>>> 270996fb6058139d0219e8f6f72d1723ce19b87e
