import paho.mqtt.client as paho
import paho.mqtt.subscribe as subscribe


broker="169.254.108.4"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))
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


client.publish("luz",payload="publish", qos=0, retain = False)

client.on_publish = on_publish 

client.loop_forever()








                           #create client object


                         #assign function to callback
                                 #establish connection
  
