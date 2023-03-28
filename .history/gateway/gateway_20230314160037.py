# print("Hello")      # Debug file

# # Import packages ###############################
# import paho.mqtt.client as mqttclient
# import json
# import time
# import serial.tools.list_ports
# import random
# import psycopg2
# from datetime import datetime
# ################ Import packages ################ 

# # DATA QUERY EXAMPLE ############################

# # conn = psycopg2.connect(database="gateway",
# #                         host="192.168.1.12",
# #                         user="postgres",
# #                         password="password",
# #                         port="5432")

# # cursor = conn.cursor()

# # current_time = datetime.now().strftime("%H:%M:%S")
# # print("Current Time =", current_time)

# # temp = "BUTTON1:ON"
# # splitData = temp.split(":")

# # cursor.execute("INSERT INTO feed_value (feed_name,timestamp,value) VALUES ('button1','"+current_time+"',1)")
# # conn.commit()
# # cursor.execute("SELECT * FROM feed_value where timestamp = '10:45:16';")
# # temp = (cursor.fetchall()[0])
# # print(temp[0])
# # cursor.close()
# # conn.close()

# ################ DATA QUERY EXAMPLE ################




# # ADAFRUIT User Information --------------------------------------
# ADAFRUIT_USERNAME = "dangnguyen"
# BROKER_ADDRESS = "io.adafruit.com"
# ADAFRUIT_ACCESS_TOKEN = "aio_sOMP53zN1nXzWToywwZ0Y5ay98ar"
# PORT = 1883
# #  ---------------------------------------------------------------



# # Adafruit feeds ------------------------------------------------------
# feed = "dangnguyen/feeds/"
# AIO_FEED_SUBCRIBE = [   "button1/",         # Fan controller
#                         "button2/",         # Light controller
#                         "FanValue/",        # Fan's rotation
#                         "LightValue/",      # Light's brightness
#                         "sensor1/",         # temperature sensor
#                         "sensor2/",         # light sensor
#                         "FanDisplay/",
#                         "LightDisplay/"]         
# AIO_FEED_PUBLISH = ["sensor1", 
#                     "sensor2",
#                     "button1", 
#                     "button2", 
#                     "FanValue", 
#                     "LightValue",
#                     "FanDisplay",
#                     "LightDisplay"]
# jsons = "json"
# feedID = {
#     "button1": 2463386,
#     "button2": 2463387,
#     "FanValue": 2463415,
#     "LightValue": 2465220,
#     "sensor1": 2462542,
#     "sensor2": 2464202,
#     "LightDisplay" : 2470613,
#     "FanDisplay" : 2470612
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

# bbc_port = find_port()
# if len(bbc_port) > 0:
#     ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# # =============================================================



# # Basic MQTT functions defined by user =======================

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
#                 client.publish(feed + AIO_FEED_PUBLISH[6], int(fanValue))
#                 cmd = "!FAN:ON:"+fanValue+"#"
        
#         if received["id"] == feedID["LightValue"]:
#             if received["last_value"] != "#":
#                 lightValue += received["last_value"]
#                 print(lightValue)
#             else: 
#                 lightValue = lightValue.replace("*", "")
                
#                 if int(lightValue) >= 100:
#                     lightValue = "100"
#                 client.publish(feed + AIO_FEED_PUBLISH[7], int(lightValue))
#                 cmd = "!LI:ON:"+lightValue+"#"

#         if received["id"] == feedID["button1"] or received["id"] == feedID["FanDisplay"] :
#             if received["last_value"] == "ON":
#                 cmd = "!FAN:ON:0#"
#             if int(received["last_value"]) > 0:
#                 cmd = "!FAN:ON:" + str(received["last_value"]) + "#"
#             if received["last_value"] == "OFF" or received["last_value"] == "0":
#                 cmd = "!FAN:OFF#"
        
#         if received["id"] == feedID["button2"] or received["id"] == feedID["LightDisplay"]:
#             if received["last_value"] == "ON":
#                 cmd = "!LI:ON:0#"
#             if int(received["last_value"]) > 0:
#                 cmd = "!LI:ON:" + str(received["last_value"]) + "#"
#             if received["last_value"] == "OFF" or received["last_value"] == "0":
#                 cmd = "!LI:OFF#"

#         if received["id"] == feedID["sensor1"]:
#             print("Temp: " + received["last_value"] + "°C")

#         if received["id"] == feedID["sensor2"]:
#             print("Light: " + received["last_value"] + " lux")

#     except: 
#         pass
#     print(cmd)
#     if len(bbc_port) > 0:
#         ser.write(str(cmd).encode())


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
#     # print(splitData)
    
#     # if splitData[0] == "TE":
#     #     client.publish(feed + AIO_FEED_PUBLISH[0], int(splitData[1]))
#     #     serial.write("!ACK:TE#".encode())

#     # if splitData[0] == "LI":
#     #     client.publish(feed + AIO_FEED_PUBLISH[1], int(splitData[1]))
#     #     serial.write("!ACK:LI#".encode())

#     # if splitData[0] == "BUT":
#     #     if splitData[1] == "1":
#     #         client.publish(feed + AIO_FEED_PUBLISH[2], (splitData[1]))
#     #         if splitData[1] == "ON":
#     #             client.publish(feed + AIO_FEED_PUBLISH[6], int(splitData[2]))
#     #         serial.write("!ACK:B1#".encode())

#     #     if splitData[2] == "2":
#     #         client.publish(feed + AIO_FEED_PUBLISH[3], (splitData[1]))
#     #         if splitData[1] == "ON":
#     #             client.publish(feed + AIO_FEED_PUBLISH[7], int(splitData[2]))
#     #         serial.write("!ACK:B2#".encode())

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

#     if len(bbc_port) >  0:
#         try:
#             readSerial()
            
#         except:
#             pass
#     time.sleep(1)




###################################### MacOS, Chrome 98. ######################################
print("Hello ThingsBoard")
import paho.mqtt.client as mqttclient
import json
import time
import serial.tools.list_ports
import re
from threading import Thread
from model import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        if "USB Serial" in txt:
            return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "4WvzYkq8gxqVnt9lOlGi"

mess = ""
global status
bbc_port = find_port()

if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=9600)

def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    global status
    print("Received: ", message.payload.decode("utf-8"))
    # temp_data = {'status': status, 'timeOfLight1': 20, 'timeOfLight2': 20}
    cmd = ""
    #TODO: Update the cmd to control the device
    try:
        jsonobj = json.loads(message.payload)
        if jsonobj['method'] == "switchMAN":
            cmd = "!!BT:000##"
        if jsonobj['method'] == "switchTUN":
            cmd = "!!BT:100##"
        if jsonobj['method'] == "setApply":
            cmd = "!!BT:200##"
        if jsonobj['method'] == "backButton":
            cmd = "!!BT:300##"
        if jsonobj['method'] == "incButton":
            cmd = "!!BT:400##"
        if jsonobj['method'] == "decButton":
            cmd = "!!BT:500##"
        if jsonobj['method'] == "resetButton":
            cmd = "!!RS:000##"

        # Adjust
        if jsonobj['method'] == "setGreen1":
            x = expand_cmd(int(jsonobj["params"]))
            cmd = "!!G1:"+ x +"##"
        if jsonobj['method'] == "setYellow1":
            x = expand_cmd(int(jsonobj["params"]))
            cmd = "!!Y1:"+ x +"##"
        if jsonobj['method'] == "setGreen2":
            x = expand_cmd(int(jsonobj["params"]))
            cmd = "!!G2:"+ x +"##"
        if jsonobj['method'] == "setYellow2":
            x = expand_cmd(int(jsonobj["params"]))
            cmd = "!!Y2:"+ x +"##"
    except:
        pass

    # print(cmd)

    if len(bbc_port) > 0:
        ser.write((str(cmd)).encode())


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Connection is failed")

def processData(data):
    '''
    !LIGHT1:TIMER_VALUE:RED1:YELLOW1:GREEN1#
    !LIGHT2:TIMER_VALUE:RED2:YELLOW2:GREEN2#
    '''

    '''
    // ACK
        /*
        * status: !!ACKSTS##
        * time: !!ACKTIM##
        * light: !!ACKLED##
        */
    '''
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    #TODO: Add your source code to publish data to the server
    if splitData[0] == 'LIGHT1':
        time1 = int(splitData[1]) if splitData[1] != "DELAY" else "DELAY"
        red1 = int(splitData[2])
        yellow1 = int(splitData[3])
        green1 = int(splitData[4])
        collect_data = {'timeOfLight1': time1, "red1": red1, "yellow1": yellow1, "green1": green1}
        client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)

    if splitData[0] == 'LIGHT2':
        ser.write("!!ACKLED##".encode())
        time2 = int(splitData[1]) if splitData[1] != "DELAY" else "DELAY"
        red2 = int(splitData[2])
        yellow2 = int(splitData[3])
        green2 = int(splitData[4])
        collect_data = {'timeOfLight2': time2, "red2": red2, "yellow2": yellow2, "green2": green2}
        client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)

    if splitData[0] == 'SET1':
        red = int(splitData[1])
        yellow = int(splitData[2])
        green = int(splitData[3])
        collect_data = {"redTime2": red, "yellowTime1": yellow, "greenTime1": green}
        client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)

    if splitData[0] == 'SET2':
        ser.write("!!ACKTIM##".encode())
        red = int(splitData[1])
        yellow = int(splitData[2])
        green = int(splitData[3])
        collect_data = {"redTime1": red, "yellowTime2": yellow, "greenTime2": green}
        client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)

    if splitData[0] == 'STATUS':
        ser.write("!!ACKSTS##".encode())
        status = int(splitData[1])
        if status in [26, 27, 28, 29]:
            status_name = "TUNING"
        elif status in [15, 16, 115, 116]:
            status_name = "MANUAL"
        else:
            status_name = "AUTO"
        collect_data = {"status": status_name}
        client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]



client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message

def ai_detect():
    counter = 1
    counter_flag = 0
    while True:
        if counter%10 == 0: 
            ai_result = detect_congesion()
            print("AI Output: ", ai_result)
            return_value, image = camera.read()
            cv2.imwrite('image/image'+ str(counter) + '.jpg', image)
        
            upload_file_list = ['image/image'+ str(counter) + '.jpg']
            gfile = drive.CreateFile({'parents': [{'id': '1fcwUjNr9pdb2BQHw8sP-esR1Iu5R3nHW'}]})
            # Read file and set it as the content of this instance.
            gfile.SetContentFile(upload_file_list[0])
            gfile.Upload() # Upload the file.
            file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1fcwUjNr9pdb2BQHw8sP-esR1Iu5R3nHW')}).GetList()
            print("https://drive.google.com/uc?export=view&id="+file_list[0]['id'])


            collect_data = {"predictCongestion": ai_result, "image": "https://drive.google.com/uc?export=view&id="+file_list[0]['id']}
            client.publish('v1/devices/me/attributes', json.dumps(collect_data), 1)
    
        
            if (counter_flag == 0):
                if ai_result.strip().split(" ")[0] == "1":
                    counter_flag = 1
                    ser.write("!!BT:100##".encode())
                    time.sleep(0.5)
                    ser.write("!!G1:100##".encode())
                    time.sleep(0.5)
                    ser.write("!!BT:200##".encode())
             
            if counter % 200 == 0:
                if counter_flag == 1:
                    if ai_result.strip().split(" ")[0] == "0":
                        counter_flag = 0
                        ser.write("!!BT:100##".encode())
                        time.sleep(0.5)
                        ser.write("!!G1:010##".encode())
                        time.sleep(0.5)
                        ser.write("!!BT:200##".encode())


        counter += 1
        time.sleep(1)

Thread(target=ai_detect).start()

while True:

    if len(bbc_port) >  0:
        try:
            readSerial()
        except:
            pass

    time.sleep(1)
