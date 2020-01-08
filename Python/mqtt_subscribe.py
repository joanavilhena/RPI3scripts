import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe
import requests
import json

webserver="http://206.189.23.62/"


broker="169.254.108.4"
port=1883

#token = '1356'
token = '4567890'
token_hub = ''

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
  pass

def ligarRega():
  pass

def ligarVentoinha():
  pass

def getSolutionData():

  print("Get solutionData")

  response = requests.get(webserver +'api/solution/token/' + token)
  if response.status_code != 200:
    print(response.status_code) 
    print(response)
    createSolution()
  else:
    print(response.json())
  
    
    
  pass


def createSolution():
  print("Create")
  url = "http://206.189.23.62/api/solution/simple"
  payload = "{\r\n    \"token\": \""+ str(token) +"\",\r\n    \"vip\": 1\r\n}"
  headers = {
    'Content-Type': 'application/json'
  }
  
  response = requests.request("POST", url, headers=headers, data = payload)

  print(response.status_code)
  
  if response.status_code != 201:
    print(response.status_code)
  else:
    #r= response.json()
    print(response.status_code)
    pass
  pass


def getServerData():
#http://206.189.23.62/api/solution/token/4567890
##########ALTERAR########
  response = requests.get(webserver +'api/solution/sensorData/' + token)
  if response.status_code != 200:
    print(response.status_code)
  else:
    r= response.json()
    print(r['sensor_data'])

  #print('{} {}'.format(r['water_force'], r['fan_force']))
  if r['sensor_data'] == '[]':
    print("no sensor data")
    #for i in r:
    #  print('{}'.format( i['id']))
    #  message = "{}:{}:1:{}".format(token,i['id'],i['value'])
    #  if(i['name']=='luz'):                           
    #    ret= client.publish("luz",message)
    #  elif(i['name']=='ambtemp'):                            
    #    ret= client.publish("ambtemp",message)
    #  elif(i['name']=='ambhum'):                               
    #    ret= client.publish("ambhum",message)
  #############################DESCONMENTAR QUANDO O TOMAS DER AS APIS######################################
      # if(b['state']=="LIGADO" && ventoinha['state']=="ON" && (i['value']>i['max_vallue']))
        #    ret= client.publish("rega","1:3")
  ##########################################################################################################
     # elif(i['name']=='solotemp'):                                
     #   ret= client.publish("solotemp",message)
     # elif(i['name']=='solohum'):                                
     #   ret= client.publish("solohum",message)
     #   if(i['value'] < i['min_value']):
      #    ret= client.publish("rega","1:3")
    # elif(i['name']=='ventoinha'):                                
    #   ret= client.publish("ventoinha",message)
    #  elif(i['name']=='rega'):                                
    #   ret= client.publish("rega",message)
      #else:
       # pass
      
  else:
    print("has data")
  pass



def on_publish(client,userdata,result):            
  #print("Updating WebServer \n") 
  pass

def createSensorDataWebServer(espID,value,topic):
  
  url = "http://206.189.23.62/api/sensorData"

  #payload = "\r\n{\"name\" : \" %s \", \" solution_id\" :  %d , \"value\": %f  , \"min_value\": 10, \"max_value\": 50}" % (topic, solutionID,value)
  payload = "\r\n{\"name\" : \""+topic+"\", \"solution_id\" : "+ token +", \"value\": "+str(value)+", \"min_value\": 10, \"max_value\": 50}"
  #"'{0}' is longer than '{1}'".format(name1, name2)
  #print("%s  %s" % (message.topic, message.payload))
  headers = {'Content-Type': 'application/json'}

  r = requests.request("POST", url, headers=headers, data = payload)

 # print(r.text.encode('utf8'))
  print(r.status_code)  

  if r.status_code != 201:
    print(r.status_code)
  else:
    print(r.status_code)
      #global token
      #token=r.json()
    print("Created")
    pass
  pass


def updateServer(espID,value,topic):
  print("Funcao UPDATE")


  url = "http://206.189.23.62/api/sensorData/update"

  payload = "{\r\n\t\"name\" : \"luz\",\r\n\t\"token\" : 2,\r\n\t\"value\": 200,\r\n    \"min_value\": 10,\r\n    \"max_value\": 50\r\n\t\r\n}"
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


def getSensor(topic,espID):
  url = "http://206.189.23.62/api/sensorData/solution/"+token+"/sensor/"+espID
  headers = {'Content-Type': 'application/json'}
  response = requests.request("GET", url, headers=headers)
  #print(response.text.encode('utf8'))
  print(response.status_code)

  if(response.status_code == 200):
    return True
  else:
    return False

def print_msg(client, userdata, message):

  print("%s  %s" % (message.topic, message.payload))
  array = message.payload.split(":")
  #solutionID = array[0]
  espID = array[1]
  value = array[2]


  if(message.topic == "rega"):
  
    ligarRega()
  elif(message.topic == "ventoinha"):
    ligarVentoinha()

  elif(getSensor(message.topic,espID)):

    if(message.topic == "luz"):                          
      print("update web server")
      print(espID)
      print(value)
      updateServer(espID,value,message.topic)                             
      #ret= client.publish("luz",str(value))
    elif (message.topic == "ambtemp" ):
      print("update web server")   
      updateServer(espID,value,message.topic)                          
      #ret= client.publish("ambtemp",str(value))
    elif (message.topic == "ambhum" ):
      print("update web server")
      updateServer(espID,value,message.topic)                             
      #ret= client.publish("ambhum",str(value))
    elif (message.topic == "solotemp" ):
      updateServer(espID,value,message.topic)
      print("update web server")                             
      #ret= client.publish("solotemp",str(value))
    elif (message.topic == "solohum" ):
      print("update web server")
      updateServer(espID,value,message.topic)                             
      #ret= client.publish("solohum",str(value))
    elif (message.topic == "ambco" ):
      print("update web server")
      updateServer(espID,value,message.topic)                             
      #ret= client.publish("ambco",str(value))
    else:
      print("Topic not valid")
      print(message.topic)  
    pass


  else:
    print("create sensor")
    createSensorDataWebServer(espID,value,message.topic)
    pass

client= paho.Client("RPI3")
client.connect(broker,port)

client.subscribe("luz",1)
client.subscribe("ambtemp",1)
client.subscribe("ambhum",1)
client.subscribe("solotemp",1)
client.subscribe("solohum",1)
client.subscribe("ambco",1)
client.subscribe("rega",1)
client.subscribe("ventoinha",1)



print("Iniciou")
getSolutionData()
getServerData()

#createSensorDataWebServer(2,4,200,"testepy")
#login()



subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos







client.loop_forever()
 
