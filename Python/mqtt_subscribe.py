import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import requests
import json

webserver="http://206.189.23.62/"


broker="169.254.108.4"
port=1883

def getServerData():
  response = requests.get(webserver +'/api/sensorData')
  r= response.json()
  
  for i in r:
    print('{} {}'.format(i['solution_id'], i['id']))
    
   # client.on_publish = on_publish                          
    #client.connect(broker,port)                                
    #ret= client.publish("luz","webOK")
    



def on_publish(client,userdata,result):             #create function for callback
    print("Updating WebServer \n")

    #Fazer update no webserver


    pass

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

    if(message.topic == 'luz'):
      print "Enviar luz para o mqtt"


    client.on_publish = on_publish                          #assign function to callback
    client.connect(broker,port)                                 #establish connection
    ret= client.publish("luz","on")
    pass


client= paho.Client("RPI3")
client.connect(broker,port)
getServerData()



subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos


client.subscribe("luz",1)
client.subscribe("ambtemp",1)
client.subscribe("ambhum",1)
client.subscribe("solotemp",1)
client.subscribe("solohum",1)
client.subscribe("ambco",1)





client.loop_forever()
 
