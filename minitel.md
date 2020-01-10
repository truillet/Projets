### Minitel : un raspberry piloté depuis un minitel (clavier et écran)
Pour ce projet, il vous faudra : 
* un minitel (1B ou 2) équipé d'une prise DIN à l'arrière
* un peu d'électronique (3 résistances de 10 kOhm, 22 kOhm et 220 kOhm et 1 transistor 2N2222) et de soudure
* un raspberry pi ([lien ici](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header))
* et deux/trois paramétrages :)

Installez tout d'abord sur une carte sd une distribution raspbian (par exemple [Buster](https://www.raspberrypi.org/downloads))

Préparez le câble entre le minitel et le raspberry (cf. schema ci dessous).

<img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/schema_minitel_rpi.png" width="400" alt="montage du cable Minitel / GPIO"> <img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/transistor.png" width="200" alt="Transistor">

Soudez les 3 fils pour le minitel à une prise DIN 5 broches (RX sur la broche 1, GND sur la broche 2 et TX sur la broche 3) et branchez les 4 fils pour le raspberry sur les broches 4 (5v), 6 (GND), 8 (TX) et 10 (RX).

<img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/GPIO_RPi.png" width="500" alt="GPIO Raspberry"> <img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/prise_DIN.png" width="300" alt="Prise DIN 5 broches">

Nous devons configurer à chaque branchement du minitel les commandes suivantes (activation du codade ASCII 7 bits et du mode echo) : 

<img src="https://github.com/truillet/Projets/blob/master/minitel/schemas/commandes_minitel.jpg" width="400" alt="commandes du Minitel / GPIO">


Il reste ensuite à indiquer au Raspberry comment permettre l'accès au terminal via la communication série.
Nous allons utiliser le script téléchargeable **(ici)[https://github.com/truillet/Projets/blob/master/minitel/getty_minitel.sh]**. Le script permet de configurer l'encodage des informations (*Nota* : nous utilisons ici une communication à 1200 bauds mais on peut monter à 4800 bauds pour un Minitel 1B et 9600 bauds pour un Minitel 2) et ouvrir un tty sur la liaison série que nous venons de configurer.
