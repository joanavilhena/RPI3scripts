import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import requests
import json

webserver="http://206.189.23.62/"


broker="169.254.108.4"
port=1883

token = ''
userID= ''
header = {'Authorization':token}

def login():
  url = "http://206.189.23.62/api/login"

  payload = "{\r\n\t\"email\" : \"tomas1@sapo.com\",\r\n\t\"password\" : \"123\",\r\n\t\r\n}"
  headers = {'Content-Type': 'application/json'}

  r = requests.request("POST", url, headers=headers, data = payload)

  print(r.text.encode('utf8'))
  
  if r.status_code != 200:
    print(r.status_code)
  else:
    global token
    token=r.json()
    getUserID()
  pass

def getUserID():
  pass




def getServerData():
  response = requests.get(webserver +'api/sensorData')
  if response.status_code != 200:
    print(response.status_code)
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

def createSensorDataWebServer(solutionID,espID,value,topic):
  
  url = "http://206.189.23.62/api/sensorData"

  #payload = "\r\n{\"name\" : \" %s \", \" solution_id\" :  %d , \"value\": %f  , \"min_value\": 10, \"max_value\": 50}" % (topic, solutionID,value)
  payload = "\r\n{\"name\" : \""+topic+"\", \"solution_id\" : "+str(solutionID)+", \"value\": 200, \"min_value\": 10, \"max_value\": 50}"
  #"'{0}' is longer than '{1}'".format(name1, name2)
  #print("%s  %s" % (message.topic, message.payload))
  headers = {'Content-Type': 'application/json'}

  r = requests.request("POST", url, headers=headers, data = payload)

  print(r.text.encode('utf8'))
  print(r.status_code)  

  if r.status_code != 200:
    print(r.status_code)
  else:
    print(r.status_code)
      #global token
      #token=r.json()
    print("Created")
    pass
  pass


def updateServer(solutionID,espID,value,topic):
  print("Funcao UPDATE")


  url = "http://206.189.23.62/api/sensorData/update"

  payload = "{\r\n\t\"name\" : \"luz\",\r\n\t\"solution_id\" : 2,\r\n\t\"value\": 200,\r\n    \"min_value\": 10,\r\n    \"max_value\": 50\r\n\t\r\n}"
  headers = {'Content-Type': 'application/json'}

  r = requests.request("POST", url, headers=headers, data = payload)

  print(r.text.encode('utf8'))
  print(r.status_code)

  if r.status_code != 201:
    print(r.status_code)
  else:
    print(r.status_code)
    #global token
    #token=r.json()
    print("Updated")
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
createSensorDataWebServer(2,4,200,"testepy")
login()



subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos







client.loop_forever()
 
