# Projets
Quelques fiches projet ...

## Raspberry Pi
Si vous souhaitez positionner manuellement la date de votre Raspberry (qui ne possède pas d'horloge par défaut), utilisez la commande suivante :

~~~~
sudo date -s "Wed Apr 10 2019 16:30:00"
~~~~

Si votre rapsberry est connecté à internet, vous pouvez préférer utiliser un serveur NTP (Network Time Protocol). Néanmoins, NTP ne mettra pas à jour l'heure si le décalage par rapport au temps courant est trop important
Il vous faudra alors modifier les options du serveur NTP comme suit :
~~~~
sudo /etc/init.d/ntp stop
sudo ntpd -q-g
sudo /etc/init.d/ntp start
~~~~	
