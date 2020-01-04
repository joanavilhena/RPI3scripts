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
    message = i['solution_id'] + ':'
    print (message) 
    if(i['name']=='luz'):  
      print(message)                            
      #ret= client.publish("luz",message)
    if(i['name']=='ambtemp'):   
      #message = i['solution_id'] + ':' + i['id'] + i['value']                             
      ret= client.publish("ambtemp",message)
    if(i['name']=='ambtemp'):                                
      ret= client.publish("ambhum","webambhumpOK")
    if(i['name']=='ambtemp'):                                
      ret= client.publish("solotemp","webambhumpOK")
    if(i['name']=='ambtemp'):                                
      ret= client.publish("ambco","webambcoOK")
    



def on_publish(client,userdata,result):             #create function for callback
    print("Updating WebServer \n")

    #Fazer update no webserver


    pass

def print_msg(client, userdata, message):

    print("%s : %s" % (message.topic, message.payload))
    array = message.payload.split(":")
    print(array)
    #pos0 = Numero da solucao pos1 numero do esp pos3 valor

    if(message.topic == 'luz'):                          
      ret= client.publish("luz","message.payload")
      #updatewebserver


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
 
