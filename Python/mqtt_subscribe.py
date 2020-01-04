import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import requests

webserver=""


broker="169.254.108.4"
port=1883

def getServerData():
  response = requests.get(webserver +'endpoint')
  print response.json()

def on_publish(client,userdata,result):             #create function for callback
    print("Updating WebServer \n")

    #Fazer update no webserver


    pass



def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))
    client.on_publish = on_publish                          #assign function to callback
    client.connect(broker,port)                                 #establish connection
    ret= client.publish("luz","on")
    pass


client= paho.Client("RPI3")
client.connect(broker,port)


subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos


client.subscribe("luz",1)
client.subscribe("ambtemp",1)
client.subscribe("ambhum",1)
client.subscribe("solotemp",1)
client.subscribe("solohum",1)


client.loop_forever()








                           #create client object


                         #assign function to callback
                                 #establish connection
  
