## Raspberry Pi "tips"
### mettre le Raspberry à l'heure
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

### eduroam avec RPi
ouvrir le fichier /etc/network/interface et ajouter les lignes suivantes

~~~~
auto lo
iface lo inet loopback

iface eth0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
~~~~

ajouter maintenant le contenu du fichier généré dans ~/.cat_installer/cat_supplicant.conf par le script python *eduroam-linux-UdT3PS.py* (cf. [https://cat.eduroam.org](https://cat.eduroam.org)) dans /etc/wpa_supplicant/wpa_supplicant.conf

