import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe


broker="169.254.108.4"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))



client1= paho.Client("RPI3")
client1.connect(broker,port)


subscribe.callback(print_msg, "#", hostname=broker)

#Subscrever topicos


client1.subscribe("test",1)



                           #create client object
client1.on_publish = on_publish 

                         #assign function to callback
                                 #establish connection
ret= client1.publish("test","on")        
