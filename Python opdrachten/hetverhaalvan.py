#geschreven door Sam Derakhshandeh
#enjoy
import os
import sys
from time import sleep


#het begin
def intro():
    text = """\n
    Mo is een jonge man van 23. Hij woont in Afghanistan.
    \n Hij leeft een rustig leven als student en studeert bij de hoge school van de hoofdstad Kabul.
    \n In Kabul leeft hij nog samen met zijn familie en hij woont dus samen met een ouders als enig kind in een klein huis.
    \n Hij houdt ook wel veel van voetbal en dat doet hij ook regelmatig buiten met zijn vrienden. 
    \n Mo wordt vaak onderdrukt vanwege zijn politieke opinies en spreekt vaak op voor zichzelf en andere. 
    \n Mo spreekt graag op voor andere en zit ook in een democratische politieke partij.
    \n Hij is wel bekend door het land en veel mensen zien hem als een perfect figuur voor de volgende electies. 
    \n Kabul is niet het beste plek om te leven maar sinds hij met zijn ouders wil blijven, is hij nog bij zijn ouders. 
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    part1()
def part1():
    text = """\n
    Het is 7 uur s ’ochtends en Mo moet naar school.
    \n Hoe zal hij naar school gaan?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Met de bus ")
    print("b). Lopend ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part2()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part3()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")   
def part2():
    text = """\n
    Hij besloot om met de bus te gaan. \n Nadat hij aankwam realiseerde hij dat hij iets te vroeg was aangekomen \n en kan hij beslissen of hij nog wat eten gaat halen of dat hij gewoon binnen in de school gaat wachten op zijn les.
    \n Zal Mo wat eten gaan halen of binnen wachten op zijn les?
 
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Wat eten gaan halen om de hoek ")
    print("b). Binnen wachten op zijn volgende les ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part4()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part5()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part3():
    text = """\n
    Sinds hij beslist om te gaan lopen naar school moet hij langs vele onveilige plekken en heeft hij der ook wat moeite mee. \n Tijdens het lopen gaat hij door zijn enkel en kan hij niet meer doorlopen. \n Er komt een auto aan met wat lijkt op een paar mannen die op weg zijn naar een moskee. 
    \n Zal Mo vragen om hulp en om een lift of hij het er gewoon proberen uit te lopen?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Je vraagt om hun hulp en vraagt ook om een lift ")
    print("b). Je gaat doorlopen en probeert het uit te lopen")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part6()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part7()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part4():
    text = """\n
    Mo is wat eten gaan halen om de hoek van zijn school en komt een prachtige jongedame tegen waar hij op het eerste oog meteen verliefd wordt. \n Maar Mo wil ook op tijd zijn voor zijn les op school. 
    \n Zal Mo hier het onbekende meisje volgen of zijn eten halen en snel terug naar school gaan?  
            """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Het onbekende meisje volgen ")
    print("b). Zijn eten halen en snel terug gaan naar school")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part8()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part9()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part5():
    text = """\n
    Mo besloot binnen te wachten voor zijn les en merkt dat er geen enkel iemand van zijn klasgenoten op school zijn. \n Hij vraagt de conciërge en die zegt dat die docent ziek is. \n Wat zal Mo op dit moment doen?
    \n Zal Mo naar huis gaan of zal hij even wat anders gaan doen?
            """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Naar huis gaan ")
    print("b). Wat anders gaan doen")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part10()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part11()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part6():
    text = """\n
      Mo vond dat hulp vragen niet kwaad kon en hield zijn hand omhoog en zwaaide in de hoop dat die auto voor hem zou stoppen. \n Ze stoppen, maar de mannen gedragen zich erg verdacht. \n Alsof ze iets willen doen. Je vindt dit erg verdacht en dit maakt je ook nerveus.
    \n Zal Mo hier toch met de auto meegaan of het proberen uit te lopen?
   """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Mo gaat ondanks zijn rare gedachtes toch mee ")
    print("b). Mo gaat het proberen uit te lopen")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part12()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part7()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part7():
    text = """\n
    Mo verstapte zich en besloot het uit te lopen. \n Hij loopt door terwijl vele mensen langs hem gaan.
    \n Hij gaat heel langzaam op dit moment denk je dat je te laat gaat komen voor je les op school.
    \n Zou je sneller willen lopen en een kans hebben om op tijd te komen met de pijn die nog hebt
    \n of wil je op te laat komen maar niks forceren op je blessure?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Sneller lopen (riskant) ")
    print("b). Langzaam lopen (veiliger) ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part13()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part14()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part8():
    text = """\n
     Hij besloot het onbekende meisje te volgen. \n
     Maar zal hij haar nummer vragen of niet?\n
     Wil je met haar spreken en haar nummer vragen?

    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Ja, vraag haar nummer ")
    print("b). Nee laat het maar zitten en ga terug naar school ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part15()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part5()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part9():
    text = """\n
     Hij besloot laatst om zijn eten te halen en terug te lopen naar school. \n Terwijl hij terugloopt naar school ziet hij iets schijnen in de lucht. \n Wat zal hij hier gaan doen? 
\n Door gaan naar school of proberen ergens anders naartoe te gaan?

    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Naar school gaan ")
    print("b). Ergens anders naartoe gaan ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part5()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part11()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part10():
    text = """\n
    Onderweg naar huis komt er een minibus langzaam aanrijden \n en Mo twijfelt waarom ze zo raar rijden sinds je de enige in de straat bent \n en je ze niet kent. 
\n Zou je hier willen vluchten of hun negeren en doorlopen?

    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Vluchten ")
    print("b). Negeren en doorlopen ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part17()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part17()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part11():
    text = """\n
    Mo beslist om wat anders te gaan doen en heeft vele dingen die hij kan doen. \n Wat zal hij doen? 
\n Toch terug gaan naar school \n of even naar het centrum van Kabul gaan?
       """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Toch terug naar school gaan ")
    print("b). Naar het centrum gaan ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part5()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part18()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part12():
    text = """\n
    Hij gaat met ze mee en het blijken erg aardige mensen te zijn en het blijkt dat ze uit dezelfde wijk als jou zijn. \n Maar onderweg zie je veel politie en later na nog wat doorrijden op de snelweg zie je militaire support wat je erg verdacht vind. 
    \n Onderweg worden jullie gestopt door de politie en je vraagt je af waarom sinds je met mensen zit de je niet kent en je altijd goed gedraagt en geen strafblad hebt. \n Maar ze vragen of we iemand hebben gezien en zeggen vervolgens Mo’s officiële volledige naam. \n Mo voelt zijn hart zinken en weet niet wat hij moet doen. 
    \n Zal Mo zeggen dat hij “die” Mo is of zal hij doen alsof hij niet weet wie dat is?

    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). De waarheid vertellen ")
    print("b). Liegen ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part20()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part21()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part13():
    text = """\n
    Hij besloot sneller te lopen met zijn blessure en is daardoor na een tijdje weer door zijn enkel gegaan \n en hij kon hier niet meer opstaan dus besloot hij te wachten op help. \n Hij is zonder zijn telefoon gegaan omdat het te riskant is om het daar te gaan meenemen (omdat het daar een arme en corrupte stad is). \n Hij kan beslissen om te wachten op de volgende keuze van auto’s die voor hem zouden stoppen.\n  Maar zal hij bij de eerste auto meteen erin gaan of de tweede auto er pas ingaan
    \n Eerste auto of de tweede auto? 
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). De eerste auto ")
    print("b). De tweede auto ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part17()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part17()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part14():
    text = """\n
Hij besloot langzamer te lopen en ondanks het langzamer lopen gaat hij weer door zijn enkel \n en hij kon hier niet meer opstaan dus besloot hij te wachten op help. \n Hij is zonder zijn telefoon gegaan omdat het te riskant is om het daar te gaan meenemen (omdat het daar een arme en corrupte stad is). \n Hij kan beslissen om te wachten op de volgende keuze van auto’s die voor hem zouden stoppen. \n Maar zal hij bij de eerste auto meteen erin gaan of de tweede auto er pas ingaan
\n Eerste auto of de tweede auto? 

    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). De eerste auto ")
    print("b). De tweede auto ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part17()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part17()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part15():
    text = """\n
    Je loopt naar haar toe en probeert haar nummer te vragen en sinds ze een fan is van je politieke meningen geeft ze je haar nummer en \n loopt ze met je door. 
    \n Wil je met haar even ergens gaan eten of wil je zelf alleen doorgaan? 
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Met haar gaan eten ")
    print("b). Zelf alleen doorgaan ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part16()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part18()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part16():
    text = """\n
    Nadat jullie een goeie restaurant hebben gevonden gaan jullie zitten en na een tijdje praten fluistert ze je hoe er een prijs op je hoofd staat en dat mensen je dood willen hebben \n en dat de president erachter zit en sinds je dat rare gevoel al had moet je meteen vluchten. \n Maar wil je haar geloven en met haar meegaan om met een smokkelaar te vluchten naar ergens veiliger \n of wil je haar niet geloven en wilt doorgaan met je leven en dan naar het centrum gaat.
    \n Wil je met haar mee of wil je doorgaan met je leven en naar het centrum gaan?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Met haar meegaan en vluchten ")
    print("b). Doorgaan met je leven en naar het centrum gaan ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end3()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part18()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part17():
    text = """\n
     Ondanks zijn keuze wordt hij ontvoerd door 5 gemaskerde mannen uit een minibus. \n Hij wordt nu ergens naartoe gebracht maar hij weet niet waar en waarom.
    \n Zal Mo het risico nemen om te proberen vrij te breken of niet?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Probeer vrij te breken ")
    print("b). Geef op ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part19()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part19()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part18():
    text = """\n
    Mo loopt nu naar het centrum van de stad en wil even wat gaan window shoppen. \n Onderweg komt er een minibus langzaam aanrijden en Mo twijfelt \n waarom ze zo raar rijden sinds je de enige in de straat bent. 
    \n Zou je hier willen vluchten of hun negeren en doorlopen?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Vluchten ")
    print("b). Negeren en doorlopen ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            part17()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part17()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")
def part19():
    text = """\n
Ondanks je keuze realiseer je je dat je omringt bent door mannen met messen en vuurwapens.
\n En sinds je bent vastgebonden kan je weinig doen.
\n Dus geef je het uiteindelijk op en wacht je het maar af.
\n Wanneer je aankomt bij wat lijkt op een kamp met mensen die trainen in zeer slechte omstandigheden.
\n Weet je niet meer waar je bent en word je gebracht naar een kleine tent waar de mensen met lange baarden
\n en de stereotypes van de terroristische groepen weet je dat je je niet meer zomaar vrij kan maken.
\n Ze vertellen je dat ze je politieke uitspraken niet oké vonden en vinden dat je je zou moeten veranderen naar hun standaarden.
\n Waarbij je allemaal dingen over hun filosofie leert en door hun wordt gebrainwashed.
\n Na een paar maanden zie je een kans waarbij ze een aanval willen plegen in Europa en
\n je wordt dan verstuurd naar een privé vliegtuig in je wordt via Yemen naar Parijs gestuurd met 3 andere van die groep.
\n Je weet dat je kans hier zit en dat je kans op overleven klein is.
\n Je probeert van ze te vluchten maar weet niet hoe.
\n En sinds je zwaar depressief bent en erg verward bent na hun brainwashen weet je niet meer wat je moet doen.
\n Maar je moet de keuze maken tussen vluchten en of de terroristische aanval te plegen.
\n Dus welke keuze ga je maken?
    """
    for char in text:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Ga vluchten naar de politie en vertel ze alles erover ")
    print("b). Ga met de andere mee en bereid je voor op een je terroristische aanval ")
    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end1()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            part20()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")

def part20():
    text = """\n
    Jouw keuze leidde tot jou en andere die zich voorbereiden op een terroristische aanval in Parijs. \n Nu zijn jullie helemaal voorbereidt en nu is er geen terug toch? \n Jullie rijden naar de Eiffeltoren en kunnen nu afschuwelijke keuze maken. \n Alles is in jouw handen en de andere wachten op jouw signaal. 
    \n Wil je het signaal geven of niet?
    """
    for char in text:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")
    sleep(1)
    incorrect = True
    print("a). Geef het signaal NIET en ga alles vertellen aan de politie die daar staat. ")
    print("b). Geef het signaal en pleeg de aanslag op de Eiffeltoren met de 3 andere ")

    awnser = input("> ")

    while incorrect == True:
        if awnser == "a":
            sleep(1)
            end2()
            incorrect = False
        elif awnser == "b":
            sleep(1)
            end4()
            incorrect = False
        else:
            print("Please pick either 'a' or 'b'")
            awnser = input("> ")

#Start van de eindes
def end1():
    text = """\n
Je wordt door de politieagenten uit de auto gesleurd en word onder arrest gezet. \n En sinds je in een land woont met een corrupt systeem, is het onmogelijk om weer vrij te komen. \n En je krijgt de doodstraf veroordeeld en je kan er niks aan doen. \n Je hebt je best gedaan.
    """
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)
    
    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")   
def end2():
    text = """\n
    Je rent naar de politie en verteld de man over alles.
    \n Je wordt onder arrestatie gezet en wordt met de andere 3 vervoerd voor toekomstig verhoor. 
    \n Je bent veroordeeld voor 42 jaar zonder uitbuiting en de andere 3 hebben levenslang gekregen.
    \n En nu ga je je leven uitzitten in het meest bewaakte gevangenis van Frankrijk.
    """
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")
def end3():
    text = """\n
Je gaat vervolgens met haar mee en later met de smokkelaars ga je verder met je reis zonder haar.
\n Je krijgt van de smokkelaar een paspoort en
\n gaat met het vliegtuig naar Griekenland waar je vanuit daar door gaat reizen naar Berlijn met de trein.
\n Zelf merkte je niet eens dat met de trein al bij Berlijn was.
\n Toen je aankwam werd je achtergelaten door de smokkelaar sinds hij zei dat hij iets ging halen.
\n Hij kwam na een paar uur niet meer terug.
\n Dus je besloot sinds je zo lang wachtte naar de politie te gaan en
\n sinds hij een neppe paspoort had werd hij naar het AZC gestuurd waar hij in proces werd gezet als vluchteling en
\n later een verblijfsvergunning kreeg door zijn herkenning door de mensen.
\n In Nederland ging hij door met zijn campagne voor meer vrijheid in Afghanistan.
    """
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")

def end4():
    text = """\n
    Je gaf het signaal en klikte dus met de andere onder de Eiffeltoren op de knop en...
    """
    for char in text:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(1)

    incorrect = True
    print("")
    print("                                        Would you like to try again?")
    print("""\
                                     [Y]: Yes                 [N]: No
        """)
    awnser = input("> ")

    while incorrect == True:
        if awnser == "YES" or awnser == "yes" or awnser == "Yes" or awnser == "Y" or awnser == "y":
            sleep(1)
            os.system("cls")
            part1()
            incorrect = False
        elif awnser == "NO" or awnser == "no" or awnser == "No" or awnser == "N" or awnser == "n":
            sleep(1)
            os.system("cls")
            incorrect = False
        else:
            sleep(0.5)
            print("                                      Please pick either 'Yes' or 'No'")
            awnser = input("> ")


intro()
