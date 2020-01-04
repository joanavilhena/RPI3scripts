import paho.mqtt.client as paho
broker="169.254.108.4"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n %s %s %s" % client, userdata, result)
    pass
client= paho.Client("RPI3)                           #create client object
client.on_publish = on_publish                          #assign function to callback
client.connect(broker,port)                                 #establish connection
ret= client.publish("luz","on")

client.loop_forever()
