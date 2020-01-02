# Projets
Quelques fiches projet ...

## Raspberry Pi
### Mettre le Raspberry à l'heure
Si vous souhaitez positionner manuellement la date de votre Raspberry (qui ne possède pas d'horloge par défaut), utilisez la commande suivante :

~~~~
sudo date -s "Wed Apr 10 2019 16:30:00"
~~~~

Si votre rapsberry est connecté à internet, vous pouvez préférer utiliser un serveur NTP (Network Time Protocol). Néanmoins, le serveur NTP ne mettra pas à jour l'heure de votre raspberry si le décalage par rapport au temps courant est trop important.
Il vous faudra alors modifier les options du serveur NTP comme suit :
~~~~
sudo /etc/init.d/ntp stop
sudo ntpd -q-g
sudo /etc/init.d/ntp start
~~~~	

### UPSSIFOX : un renard qui parle 
Pour ce projet, il vous faudra
* un raspberry pi zero W ([lien ici](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header)) équipé de hauts-parleurs (comme le [pHAT Speaker](https://shop.pimoroni.com/products/speaker-phat))
* une batterie (comme celle-là)
* et un peu de logiciel (voir plus bas)


