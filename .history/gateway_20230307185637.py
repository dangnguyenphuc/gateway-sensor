# ###################################### MacOS, Chrome 98. ######################################
# print("Hello")
# import paho.mqtt.client as mqttclient
# import json
# import time
# import serial.tools.list_ports
# import random

# '''
# 	@name: find_port()
# 	@param:
# 		None
# 	@exp:
# 		from Serial, received data will be processed and pushed to Adafruit.
# '''
# # def find_port():
# #     for port in list(serial.tools.list_ports.comports()):
# #         txt = str(port)
# #         if "USB Serial" in txt:
# #             return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

# ADAFRUIT_ACCESS_TOKEN = "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn"
# ADAFRUIT_USERNAME = "dangnguyen"
# BROKER_ADDRESS = "io.adafruit.com"
# PORT = 1883

# # feeds ---------------------------------------------------------------
# feed = "dangnguyen/feeds/"
# AIO_FEED_INPUT = ["button1/", "button2/", "FanValue/", "LightValue/"]
# AIO_FEED_PUBLISH = ["sensor1", "sensor2",]
# jsons = "json"
# feedID = {
#     "button1": 2463386,
#     "button2": 2463387,
#     "FanValue": 2463415,
#     "LightValue": 2465220
# }
# # ---------------------------------------------------------------------

# mess = ""
# fanValue = ""
# lightValue = ""


# # bbc_port = find_port()
# # if len(bbc_port) > 0:
# #     ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# def subscribed(client, userdata, mid, granted_qos):
#     print("Subscribed...")


# def recv_message(client, userdata, message):
#     global fanValue, lightValue
#     received =  json.loads(message.payload.decode("utf-8"))
#     cmd = "" 
#     print("Received from: " + str(received['id']))
#     #TODO: Update the cmd to control the device
#     try:
#         if received["id"] == feedID["FanValue"]:
#             if received["last_value"] != "#":
#                 fanValue += received["last_value"]
#                 print(fanValue)
#             else: 
#                 fanValue = fanValue.replace("*", "")
                
#                 if int(fanValue) >= 100:
#                     fanValue = "100"

#                 cmd = "!FAN:ON:"+fanValue+"#"
        
#         if received["id"] == feedID["LightValue"]:
#             if received["last_value"] != "#":
#                 lightValue += received["last_value"]
#                 print(lightValue)
#             else: 
#                 lightValue = lightValue.replace("*", "")
                
#                 if int(lightValue) >= 100:
#                     lightValue = "100"

#                 cmd = "!LI:ON:"+lightValue+"#"

#         if received["id"] == feedID["button1"]:
#             if received["last_value"] == "ON":
#                 cmd = "!FAN:ON:0#"
#             if received["last_value"] == "OFF":
#                 cmd = "!FAN:OFF#"
        
#         if received["id"] == feedID["button2"]:
#             if received["last_value"] == "ON":
#                 cmd = "!LI:ON:0#"
#             if received["last_value"] == "OFF":
#                 cmd = "!LI:OFF#"

#     except: 
#         pass
#     print(cmd)

# #     if len(bbc_port) > 0:
# #         ser.write((str(cmd)).encode())


# def connected(client, userdata, flags, rc):
#         try:
#             print("Connected successfully!!")
#             for topic in AIO_FEED_INPUT:
#                 client.subscribe(feed+topic+jsons)
#         except:
#             print("Connection is failed")
#             pass

# '''
# 	@name: processData()
# 	@param:
# 		data: string
# 	@exp:
# 		from Serial, received data will be processed and pushed to Adafruit.
# '''
# def processData(data):
#     data = data.replace("!", "")
#     data = data.replace("#", "")
#     splitData = data.split(":")
#     print(splitData)
    
#     if splitData[0] == "TEMP":
#         client.publish(feed + AIO_FEED_PUBLISH[0], int(splitData[1]))
#   		serial.write("!ACK:TE#".encode())

# 	if splitData[0] == "LI":
#         client.publish(feed + AIO_FEED_PUBLISH[1], int(splitData[1]))
#   		serial.write("!ACK:LI#".encode())
   		 

# def readSerial():
#     bytesToRead = ser.inWaiting()
#     if (bytesToRead > 0):
#         global mess
#         mess = mess + ser.read(bytesToRead).decode("UTF-8")
#         while ("#" in mess) and ("!" in mess):
#             start = mess.find("!")
#             end = mess.find("#")
#             processData(mess[start:end + 1])
#             if (end == len(mess)):
#                 mess = ""
#             else:
#                 mess = mess[end+1:]



# client = mqttclient.Client("Gateway_Adafruit")
# client.username_pw_set(ADAFRUIT_USERNAME, ADAFRUIT_ACCESS_TOKEN)


# client.connect(BROKER_ADDRESS, 1883)

# client.on_connect = connected
# client.loop_start()

# client.on_subscribe = subscribed
# client.on_message = recv_message
# while True:

#     # if len(bbc_port) >  0:
#     #     try:
#     #         readSerial()
            
#     #     except:
#     #         pass
#     time.sleep(1)

import psycopg2
conn = psycopg2.connect(database="sensor_data",
                        host="localhost",
                        user="postgres",
                        password="password",
                        port="5432")