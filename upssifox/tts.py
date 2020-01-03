#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import paho.mqtt.client as paho # import Paho
import time
import os

############
def on_message(client, userdata, message):
#    print("message received " ,str(message.payload.decode("utf-8")))
#    print("message topic=",message.topic)

# suivant le topic
    if (message.topic == "/renard/tts"):
        os.system("espeak -vfr -s140 \"" + str(message.payload.decode("utf-8")) + "\" 2>/dev/null") # use external tool      
	client.publish("/renard/feedback", "tts done")
    elif (message.topic == "/renard/wav"):
        os.system("aplay ./sounds/" + str(message.payload.decode("utf-8")) + ".wav")
        client.publish("/renard/feedback", "wav done")
	
########################################
broker_address="localhost"

print("creating new instance")
client = paho.Client(client_id="Renard") # create new instance
client.on_message = on_message # attach function to callback

print("connecting to broker")
client.connect(broker_address) # connect to broker
client.subscribe("/renard/tts")
print("connected to broker")

while client.loop()==0: # start the loop
	time.sleep(1)

