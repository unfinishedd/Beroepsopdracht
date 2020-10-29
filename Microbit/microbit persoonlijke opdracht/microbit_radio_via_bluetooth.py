#enjoy
from microbit import *
import radio

radio.on()
# de andere microbit moet ook zijn radio kanaal op 22 zetten
radio.config(channel=22)

# dit is voor hoe ver het de microbit het bericht kan versturen van 0 tot 7
radio.config(power=7)

message_to_master = " Drink wat meer gefrituurd water, dat is wat biologischer. "

# deze code is voor een bericht sturen
radio.send(message_to_master)

#hieronder is de code voor als je een code wilt ontvangen
#message_received = radio.receive()

#dit is voor de loop 
while True:
    radio.send(message_to_master)
    incoming = radio.receive()

if incoming is not None:
    display.show(incoming)
    print(incoming)
sleep(500)



# Ik kwam er trouwens achter dat een microbit met iphones zou kunnen koppelen
# via de bluetooth, als er alleen wat meer ram in zat.


# ik kon alleen de video niet maken omdat ik geen 2 microbits heb
# maar ik kan het wel een keer laten zien
