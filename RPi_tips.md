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
ouvrir le fichier /etc/network/interfaces et ajouter les lignes suivantes

~~~~
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback

iface eth0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
~~~~

exécuter le script python *eduroam-linux-UdT3PS.py* (téléchargé depuis  [https://cat.eduroam.org](https://cat.eduroam.org))

ouvrir le fichier /etc/wpa_supplicant/wpa_supplicant.conf et complétez avec les lignes suivantes

~~~~
network={
ssid="eduroam"
key_mgmt=WPA-EAP
pairwise=CCMP
eap=PEAP TTLS
identity="YOUR-IDENTITY"
anonymous_identity="anonymous@univ-tlse3.fr"
password="YOUR-PASSWORD"
phase1="peaplabel=0"
phase2="auth=MSCHAPV2"
priority=999
}
~~~
