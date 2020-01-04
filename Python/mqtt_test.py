import paho.mqtt.client as paho
broker="169.254.108.4"
port=1883


#Subscrever topicos
client1.subscribe("test",1)



def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass


client1= paho.Client("RPI3")                           #create client object
client1.on_publish = on_publish 

                         #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("test","on")        
