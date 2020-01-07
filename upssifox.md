### UPSSIFOX : un renard qui parle 
Pour ce projet, il vous faudra : 
* un raspberry pi zero W ([lien ici](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header)) équipé de hauts-parleurs (comme le [pHAT Speaker](https://shop.pimoroni.com/products/speaker-phat))
* une batterie (comme [celle-là](https://www.amazon.fr/Anker-Batterie-PowerCore-Technologies-VoltageBoost/dp/B01CU1EC6Y/ref=asc_df_B01CU1EC6Y/?tag=googshopfr-21&linkCode=df0&hvadid=167156500272&hvpos=1o1&hvnetw=g&hvrand=3009678357010748596&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9055254&hvtargid=pla-159638380810&psc=1))
* un peu de codage (voir plus bas)
* et une peluche ;) (par exemple, [celle là](https://www.amazon.fr/gp/product/B07QW1RC56/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1))

Installez tout d'abord sur une carte sd une distribution raspbian (par exemple [Buster](https://www.raspberrypi.org/downloads))
Procédez ensuite à l'installation de :
* RaspAP (hotspot wifi)
* mosquitto (broker MQTT)
* librairie paho-mqtt pour moquitto
* espeak (tts)
* la librairie speakerphat

~~~~
curl -sL https://install.raspap.com | bash
sudo apt-get install mosquitto 
sudo pip3 install paho-mqtt 
sudo apt-get install espeak
curl -sS https://get.pimoroni.com/speakerphat | bash
~~~~	

Positionnez le script [tts.py](https://github.com/truillet/Projets/blob/master/upssifox/tts.py) et [launcher.sh](https://github.com/truillet/Projets/blob/master/upssifox/launcher.sh) à la racine /home/pi. Lancez les commandes suivantes
~~~~
chmod 755 launcher.sh
mkdir logs
sudo crontab -e
~~~~

Ajoutez la ligne suivante :
~~~~
@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1
~~~~
