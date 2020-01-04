import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import requests
import json

webserver="http://206.189.23.62/"


broker="169.254.108.4"
port=1883

token = ''
header = {'Authorization':token}

def login():
  data = {'email': 'tomas1@sapo.com', 'password': '123' }
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  r = requests.post(webserver + "api/login", data=json.dumps(data), headers=headers)
  token = requests.json()
  print(r.status_code)
  pass

def getServerData():
  response = requests.get(webserver +'/api/sensorData')
  r= response.json()
  
  for i in r:
    print('{} {}'.format(i['solution_id'], i['id']))
    message = "{}:{}:{}".format(i['solution_id'],i['id'],i['value'])
    if(i['name']=='luz'):                           
      ret= client.publish("luz",message)
    if(i['name']=='ambtemp'):                            
      ret= client.publish("ambtemp",message)
    if(i['name']=='ambtemp'):                                
      ret= client.publish("ambhum",message)
    if(i['name']=='ambtemp'):                                
      ret= client.publish("solotemp",message)
    if(i['name']=='ambtemp'):                                
      ret= client.publish("ambco",message)
  pass
    



def on_publish(client,userdata,result):            
  print("Updating WebServer \n")
  #Fazer update no webserver

   
  pass

def print_msg(client, userdata, message):

  print("%s : %s" % (message.topic, message.payload))
  array = message.payload.split(":")
  solutionID = array[0]
  espID = array[1]
  value = array[2]
  print(solutionID)
    

  if(message.topic == 'luz'):                          
    ret= client.publish("luz","message.payload")
      #updatewebserver
    print("update web server")
    client.on_publish = on_publish                          
    client.connect(broker,port)                                 
    #ret= client.publish("luz","on")
  pass


client= paho.Client("RPI3")
client.connect(broker,port)
getServerData()
login()



subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos


client.subscribe("luz",1)
client.subscribe("ambtemp",1)
client.subscribe("ambhum",1)
client.subscribe("solotemp",1)
client.subscribe("solohum",1)
client.subscribe("ambco",1)





client.loop_forever()
 
