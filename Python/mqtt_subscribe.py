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
  if r.status_code != 200:
    print(r.status_code)
  else:
    global token
    token=r.json()
  pass

def getServerData():
  response = requests.get(webserver +'api/sensorData')
  if response.status_code != 200:
    print(r.status_code)
  else:
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
  #print("Updating WebServer \n") 
  pass

def updateServer(solutionID,espID,value,topic):
  print("Funcao UPDATE")
  print(solutionID)
  print(espID)
  print(value)
  print(topic)
  r = requests.get(webserver +'api/sensorData/solution' + solutionID + '/sensor/' + espID)
  if r.status_code != 200:
    print(r.status_code)
  else:
    r= r.json()
    print(r)


  data = {}
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  r = requests.post(webserver + "api/login", data=json.dumps(data), headers=headers)
  if r.status_code != 200:
    print(r.status_code)
  else:
    global token
    token=r.json()
    pass
  pass

def print_msg(client, userdata, message):

  print("%s  %s" % (message.topic, message.payload))
  array = message.payload.split(":")
  solutionID = array[0]
  espID = array[1]
  value = array[2]
    
  if(message.topic == "luz"):                          
    print("update web server")
    print(solutionID)
    print(espID)
    print(value)
    updateServer(solutionID,espID,value,message.topic)                             
    #ret= client.publish("luz",str(value))
  elif (message.topic == "ambtemp" ):
    print("update web server")                             
    #ret= client.publish("ambtemp",str(value))
  elif (message.topic == "ambhum" ):
    print("update web server")                             
    #ret= client.publish("ambhum",str(value))
  elif (message.topic == "solotemp" ):
    print("update web server")                             
    #ret= client.publish("solotemp",str(value))
  elif (message.topic == "solohum" ):
    print("update web server")                             
    #ret= client.publish("solohum",str(value))
  elif (message.topic == "ambco" ):
    print("update web server")                             
    #ret= client.publish("ambco",str(value))
  else:
    print("Topic not valid")
    print(message.topic)  
  pass


client= paho.Client("RPI3")
client.connect(broker,port)

client.subscribe("luz",1)
client.subscribe("ambtemp",1)
client.subscribe("ambhum",1)
client.subscribe("solotemp",1)
client.subscribe("solohum",1)
client.subscribe("ambco",1)

getServerData()
login()



subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos







client.loop_forever()
 
