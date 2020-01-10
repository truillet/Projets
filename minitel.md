### Minitel : un raspberry piloté depuis un minitel (clavier et écran)
Pour ce projet, il vous faudra : 
* un minitel (1B ou 2) équipé d'une prise DIN à l'arrière
* un peu d'électronique (3 résistances de 10 kOhm, 22 kOhm et 220 kOhm et 1 transistor 2N2222) et de soudure
* un raspberry pi ([lien ici](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header))
* et deux/trois paramétrages :)

Installez tout d'abord sur une carte sd une distribution raspbian (par exemple [Buster](https://www.raspberrypi.org/downloads))

Préparez le câble entre le minitel et le raspberry (cf. schema ci dessous).

<img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/schema_minitel_rpi.png" width="400" alt="montage du cable Minitel / GPIO">

Soudez les 3 fils pour le minitel à une prise DIN 5 broches et branchez les broches 4 (5v), 6 (GND), 8 (TX) et 10 (RX) sur le raspberry.

<img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/GPIO_RPi.png" width="500" alt="GPIO Raspberry">

Il reste ensuite à indiquer au Raspberry comment permettre l'accès au terminal via la communication série.
