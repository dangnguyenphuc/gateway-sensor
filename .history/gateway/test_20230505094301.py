# print("Hello")      # Debug file

# # Import packages ###############################
# import paho.mqtt.client as mqttclient
# import json
# import time
# import serial.tools.list_ports
# import random
# import pymongo
# from pymongo import MongoClient
# from datetime import datetime
# ################ Import packages ################ 

# # DATA QUERY EXAMPLE ############################

# # current_time = datetime.now().strftime("%d,%b.%H:%M:%S")

# client = MongoClient('mongodb+srv://dangnguyenblackie:dang1012@cluster0.ricdizx.mongodb.net/?retryWrites=true&w=majority')
#     # database 
# db = client["SmartHome"]
#     # collection
# fan_collection = db["Fan"]
# Bulb_collection = db["Bulb"]
# Door_collection = db["Door"]
# sensor_collection = db["sensors"]


# # fan_collection.delete_many({})
# # Bulb_collection.delete_many({})
# # sensor_collection.delete_many({})
# # Door_collection.delete_many({})

# # res = user_collection.find().sort("id",-1).limit(1)
# # fan_collection.insert_one({"_id": 2, "timestamp": f'{current_time}', "status": "OFF", "value" : 0})
# # print(res[0]['firstName'])
# # sensor_collection.insert_one({"timestamp": f'{current_time}', "temp": float('23.7'), "light" : float('32')})
# ################ DATA QUERY EXAMPLE ################




# # ADAFRUIT User Information --------------------------------------
# ADAFRUIT_USERNAME = "dangnguyen"
# BROKER_ADDRESS = "io.adafruit.com"
# ADAFRUIT_ACCESS_TOKEN = "aio_DsnO87BT3KLJ5mdsLQ5BS7RXp0hY"
# PORT = 1883
# #  ---------------------------------------------------------------



# # Adafruit feeds ------------------------------------------------------
# feed = "dangnguyen/feeds/"
# AIO_FEED_SUBCRIBE = [   "nmdk-1-fanstatus-1/",      # Fan controller
#                         "nmdk-1-ledstatus-1/",      # Light controller
#                         "nmdk-1-doorstatus-1/",     # Door controller
#                         "nmdk-1-fanvalue-1/",       # Fan's rotation
#                         "nmdk-1-ledvalue-1/",       # Light's brightness
#                         "nmdk-1-soundai/"
#                     ]    

# AIO_FEED_PUBLISH = [    
#                         "nmdk-1-tempsensor-1",         # temperature sensor
#                         "nmdk-1-lightsensor-1",         # light sensor
#                         "nmdk-1-fanstatus-1",         # Fan controller
#                         "nmdk-1-ledstatus-1",         # Light controller
#                         "nmdk-1-doorstatus-1",         # Door controller
#                         "nmdk-1-fanvalue-1",
#                         "nmdk-1-ledvalue-1",
#                         "nmdk-1-soundai"
#                         ]    

# jsons = "json"
# feedID = {
#     "nmdk-1-fanstatus-1": 2514720,
#     "nmdk-1-ledstatus-1": 2514722,
#     "nmdk-1-doorstatus-1": 2514719,
#     # "nmdk-1-tempsensor-1": 2462542,
#     # "nmdk-1-lightsensor-1": 2464202,
#     "nmdk-1-ledvalue-1" : 2514723,
#     "nmdk-1-fanvalue-1" : 2514721,
#     "nmdk-1-soundai" : 2514725
# }
# # ---------------------------------------------------------------------



# # message received by serial ------------------------------------------
# mess = ""
# fanValue = ""
# lightValue = ""
# # ---------------------------------------------------------------------



# # Get serial port =======================

# '''
#     @name: find_port()
#     @param:
#         None
#     @exp:
#         Find serial port connects to YOLO:bit.
# '''
# def find_port():
#     for port in list(serial.tools.list_ports.comports()):
#         txt = str(port)
#         if "USB Serial" in txt:
#             return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

# # bbc_port = find_port()
# # if len(bbc_port) > 0:
# #     ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# # =============================================================



# # Basic MQTT functions defined by user =======================

# def subscribed(client, userdata, mid, granted_qos):
#     print("Subscribed...")


# def recv_message(client, userdata, message):
#     global fanValue, lightValue
#     received =  json.loads(message.payload.decode("utf-8"))
#     current_time = datetime.now().strftime("%d,%b.%H:%M:%S")
#     cmd = "" 
#     print("Received from: " + str(received['id']))
#     print(message)
# #     #TODO: Update the cmd to control the device
# #     try:
# #         if received["id"] == feedID["FanValue"]:
# #             if received["last_value"] != "#":
# #                 fanValue += received["last_value"]
# #                 print(fanValue)
# #             else: 
# #                 fanValue = fanValue.replace("*", "")
                
# #                 if int(fanValue) >= 100:
# #                     fanValue = "100"
# #                 # client.publish(feed + AIO_FEED_PUBLISH[6], int(fanValue))
# #                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": int(fanValue)})
# #                 cmd = "!FAN:ON:"+fanValue+"#"
        
# #         if received["id"] == feedID["LightValue"]:
# #             if received["last_value"] != "#":
# #                 lightValue += received["last_value"]
# #                 print(lightValue)
# #             else: 
# #                 lightValue = lightValue.replace("*", "")
                
# #                 if int(lightValue) >= 100:
# #                     lightValue = "100"
# #                 # client.publish(feed + AIO_FEED_PUBLISH[7], int(lightValue))
# #                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": int(lightValue)})
# #                 cmd = "!LI:ON:"+lightValue+"#"

# #         if received["id"] == feedID["button1"]:
# #             if received["last_value"] == "ON":
# #                 cmd = "!FAN:ON:0#"
# #                 client.publish(feed + AIO_FEED_PUBLISH[6], int(40))
# #                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": 40})
# #             if received["last_value"] == "OFF":
# #                 cmd = "!FAN:OFF#"
# #                 client.publish(feed + AIO_FEED_PUBLISH[6], int(0))
# #                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})

# #         if received["id"] == feedID["FanDisplay"]:
# #             if int(received["last_value"]) > 0:
# #                 cmd = "!FAN:ON:" + str(received["last_value"]) + "#"
# #                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": int(received["last_value"])})
# #             if int(received["last_value"]) == 0:
# #                 cmd = "!FAN:OFF#"
# #                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})

# #         if received["id"] == feedID["button2"]:
# #             if received["last_value"] == "ON":
# #                 cmd = "!LI:ON:0#"
# #                 client.publish(feed + AIO_FEED_PUBLISH[7], int(40))
# #                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": 40})
# #             if received["last_value"] == "OFF":
# #                 cmd = "!LI:OFF#"
# #                 client.publish(feed + AIO_FEED_PUBLISH[7], int(0))
# #                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})
        
# #         if received["id"] == feedID["button3"]:
# #             if received["last_value"] == "ON":
# #                 cmd = "!DO:ON#"
# #                 Door_collection.insert_one({"timestamp": f'{current_time}', "status": "ON"})
# #             if received["last_value"] == "OFF":
# #                 cmd = "!DO:OFF#"
# #                 Door_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF"})

# #         if received["id"] == feedID["LightDisplay"]:
# #             if int(received["last_value"]) > 0:
# #                 cmd = "!LI:ON:" + str(received["last_value"]) + "#"
# #                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "ON", "value": int(received["last_value"])})
# #             if int(received["last_value"]) == 0:
# #                 cmd = "!LI:OFF#"
# #                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})
# # # DEBUG ==========================================================
# #         # if received["id"] == feedID["sensor1"]:
# #         #     print("Temp: " + received["last_value"] + "°C")

# #         # if received["id"] == feedID["sensor2"]:
# #         #     print("Light: " + received["last_value"] + " lux")
# # # DEBUG ==========================================================
# #     except: 
# #         pass
# #     if len(bbc_port) > 0:
# #         ser.write(str(cmd).encode())


# def connected(client, userdata, flags, rc):
#         try:
#             print("Connected successfully!!")
#             for topic in AIO_FEED_SUBCRIBE:
#                 client.subscribe(feed+topic+jsons)
#                 print("Connected to " + topic + " successfully!!")
#         except:
#             print("Connection is failed")
#             pass

# # ===================================================



# # Serial process ------------------------------------

# '''
#     @name: processData()
#     @param:
#         data: string
#     @exp:
#         from Serial, received data will be processed and pushed to Adafruit.
# '''
# def processData(data):
#     print(data)
#     data = data.replace("!", "")
#     data = data.replace("#", "")
#     splitData = data.split(":")
#     print(splitData)
#     current_time = datetime.now().strftime("%d,%b.%H:%M:%S")
#     if splitData[0] == "TE" and splitData[2] == "LI":
#         client.publish(feed + AIO_FEED_PUBLISH[0], float(splitData[1]))
#         client.publish(feed + AIO_FEED_PUBLISH[1], float(splitData[3]))
#         sensor_collection.insert_one(
#                 {
#                     "timestamp": f'{current_time}', 
#                     "temp": float(splitData[1]),        
#                     "light" : float(splitData[3])
#                 }
#             )
#         ser.write("!ACK:TELI#".encode())

#     if splitData[0] == "BUT":
#         if splitData[1] == "1":
#             client.publish(feed + AIO_FEED_PUBLISH[2], (splitData[2]))
#             if splitData[2] == "ON":
#                 client.publish(feed + AIO_FEED_PUBLISH[5], int(splitData[3]))
#                 fan_collection.insert_one(
#                         {
#                             "timestamp": f'{current_time}', 
#                             "status": "ON", 
#                             "value": int(splitData[3])
#                         }
#                     )
#             else: 
#                 client.publish(feed + AIO_FEED_PUBLISH[5], 0)
#                 fan_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})
#             ser.write("!ACK:B1#".encode())

#         if splitData[1] == "2":
#             client.publish(feed + AIO_FEED_PUBLISH[3], (splitData[2]))
#             if splitData[2] == "ON":
#                 client.publish(feed + AIO_FEED_PUBLISH[6], int(splitData[3]))
#                 Bulb_collection.insert_one(
#                         {
#                             "timestamp": f'{current_time}', 
                            
#                             "status": "ON", 
#                             "value": int(splitData[3])
#                         }
#                     )
#             else: 
#                 client.publish(feed + AIO_FEED_PUBLISH[6], 0)
#                 Bulb_collection.insert_one({"timestamp": f'{current_time}', "status": "OFF", "value": 0})
#             ser.write("!ACK:B2#".encode())

#         if splitData[1] == "3":
#             client.publish(feed + AIO_FEED_PUBLISH[4], 0)
#             Door_collection.insert_one(
#                     {
#                         "timestamp": f'{current_time}', 
#                         "status": splitData[1]
#                     }
#                 )
#             ser.write("!ACK:B3#".encode())

# '''
#     @name: readSerial()
#     @param:
#         None
#     @exp:
#         Receiving data by readind byte to byte, and each message is between "!" and "#" characters.
# '''
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

# # --------------------------------------------------------------------



# ######################## PAHO-MQTT CONNECTION ########################
# # define client
# client = mqttclient.Client("Gateway_Adafruit")

# # set username and password
# client.username_pw_set(ADAFRUIT_USERNAME, ADAFRUIT_ACCESS_TOKEN)

# # connect to broker with address and port
#     # Port:
#         # 1883: Insecure port.
#         # 8883: Secure port.
#         # 443: MQTT through Websocket. 
# client.connect(BROKER_ADDRESS, 1883)


# # subcribe and receive data from server. _________
# client.on_connect = connected
# client.loop_start()
# client.on_subscribe = subscribed
# client.on_message = recv_message
# # ________________________________________________

# ######################## DONE ########################

# '''
#     Enter while loop.
# '''
# while True:

#     # if len(bbc_port) >  0:
#     #     try:
#     #         readSerial()
            
#     #     except:
#     #         pass

#     # client.publish(feed + AIO_FEED_PUBLISH[0], 101)
#     # client.publish(feed + AIO_FEED_PUBLISH[1], 112)
#     # client.publish(feed + AIO_FEED_PUBLISH[2], "ON")
#     # client.publish(feed + AIO_FEED_PUBLISH[3], "OFF")
#     # client.publish(feed + AIO_FEED_PUBLISH[4], "ON")
#     # client.publish(feed + AIO_FEED_PUBLISH[5], 13)
#     # client.publish(feed + AIO_FEED_PUBLISH[6], 45)
#     client.publish(feed + AIO_FEED_PUBLISH[7], "FAN_ON")
#     time.sleep(5)

sentences = [
    "Could you please open the door for me?",
    "Would you mind opening the door?",
    "Can you open the door, please?",
    "I need you to open the door for me.",
    "Could you do me a favor and open the door?",
    "Can you please let me in by opening the door?",
    "Would it be possible for you to open the door?",
    "I'm unable to open the door, could you help me?",
    "Can you open the door so that I can come in?",
    "Please open the door, I need to get inside.",
    "Could you please unlock the door and let me in?",
    "Can you please open the door for me, it's urgent?",
    "I forgot my keys, could you open the door for me?",
    "Can you open the door, I have my hands full.",
    "I'm locked out, could you please open the door?",
    "Please open the door, I have important news to share.",
    "Could you open the door, it's very cold outside.",
    "Could you open the door, I'm running late.",
    "Can you please open the door for me, I have a delivery.",
    "Would you be so kind as to open the door for me?",
    "I'm stuck outside, could you please open the door?",
    "Can you open the door, I need to use the restroom.",
    "Please open the door, I need to speak with you.",
    "Could you open the door, I have a surprise for you.",
    "Can you please open the door, I'm carrying something heavy.",
    "Would you mind opening the door, I need to come in.",
    "Please unlock the door and let me in.",
    "Could you open the door, I'm soaked from the rain.",
    "Can you open the door, I left something inside.",
    "Please open the door, I need to get my coat.",
    "Could you do me a favor and open the door for me?",
    "Can you please open the door, I have a question to ask.",
    "I'm locked out, could you please open the door for me?",
    "Please open the door, I need to grab something quickly.",
    "Could you open the door, I'm feeling sick.",
    "Can you please open the door, I need to make a call.",
    "I left my phone inside, could you please open the door?",
    "Please open the door, I need to get to my appointment.",
    "Could you open the door, I'm in a hurry.",
    "Can you please open the door, I need to get to work.",
    "I'm locked out, could you please open the door for me?",
    "Please open the door, I have a surprise for you.",
    "Could you open the door, I need to get my keys.",
    "Can you please open the door, I have a gift for you.",
    "Please unlock the door and let me in, I forgot my access card.",
    "Could you open the door, I need to grab a document.",
    "Can you please open the door, I need to go to the bank.",
    "Please open the door, I need to speak with your manager.",
    "Could you open the door, I have a package for you.",
    "Can you please open the door, I need to check something.",
    "Please unlock the door and let me in, I need to use the printer.",
    "Could you open the door, I need to get my laptop.",
    "Can you please open the door, I need to get to the airport.",
    "Please open the door, I need to pick up my kids.",
    "Could you open the door, I need to get to my class.",
    "Can you please open the door, I need to get to my meeting.",
    "Please unlock the door and let me in, I need to get to my locker.",
    "Could you open the door, I need to get to my car.",
    "Can you please open the door, I need to get to the gym.",
    "Please open the door, I have some important documents to show you.",
    "Could you open the door, I need to get to my appointment.",
    "Can you please open the door, I need to get some fresh air.",
    "Please unlock the door and let me in, I need to use the restroom.",
    "Could you open the door, I need to get to my therapy session.",
    "Can you please open the door, I need to get to my yoga class.",
    "Please open the door, I need to get to my hair appointment.",
    "Could you open the door, I need to get to my doctor's appointment.",
    "Can you please open the door, I need to get to my dentist's appointment.",
    "Please unlock the door and let me in, I need to get to my eye appointment.",
    "Could you open the door, I need to get to my physiotherapy session.",
    "Can you please open the door, I need to go to the post office.",
    "Please open the door, I need to get to my music lesson.",
    "Could you open the door, I need to get to my language class.",
    "Can you please open the door, I need to go to the grocery store.",
    "Please unlock the door and let me in, I need to get to my dance class.",
    "Could you open the door, I need to get to my cooking class.",
    "Can you please open the door, I need to get to my painting lesson.",
    "Please open the door, I need to get to my pottery class.",
    "Could you open the door, I need to get to my photography class.",
    "Can you please open the door, I need to get to my writing class.",
    "Please unlock the door and let me in, I need to get to my singing lesson.",
    "Could you open the door, I need to get to my acting class.",
    "Can you please open the door, I need to get to my sports training.",
    "Please open the door, I need to get to my swimming lesson.",
    "Could you open the door, I need to get to my martial arts class.",
    "Can you please open the door, I need to get to my fencing lesson.",
    "Please unlock the door and let me in, I need to get to my archery lesson."
]

with open("gateway/light0.txt","w") as f:
    for i in sentences:
        f.write('"' + i +'"' + "," + "5\n")
    print("D")