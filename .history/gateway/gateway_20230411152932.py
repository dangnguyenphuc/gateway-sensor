print("Hello")      # Debug file

# Import packages ###############################
import paho.mqtt.client as mqttclient
import json
import time
import serial.tools.list_ports
import random
import pymongo
from pymongo import MongoClient
from datetime import datetime
################ Import packages ################ 

# DATA QUERY EXAMPLE ############################

# current_time = datetime.now().strftime("%d,%b.%H:%M:%S")

client = MongoClient('mongodb+srv://dangnguyenblackie:dang1012@cluster0.ricdizx.mongodb.net/?retryWrites=true&w=majority')
    # database 
db = client["SmartHome"]
    # collection
fan_collection = db["Fan"]
Bulb_collection = db["Bulb"]
Door_collection = db["Door"]
sensor_collection = db["sensors"]


# fan_collection.delete_many({})
# Bulb_collection.delete_many({})
# sensor_collection.delete_many({})
# Door_collection.delete_many({})

# res = user_collection.find().sort("id",-1).limit(1)
# fan_collection.insert_one({"_id": 2, "timestamp": f'{current_time}', "status": "OFF", "value" : 0})
# print(res[0]['firstName'])
# sensor_collection.insert_one({"timestamp": f'{current_time}', "temp": float('23.7'), "light" : float('32')})
################ DATA QUERY EXAMPLE ################




# ADAFRUIT User Information --------------------------------------
ADAFRUIT_USERNAME = "dangnguyen"
BROKER_ADDRESS = "io.adafruit.com"
ADAFRUIT_ACCESS_TOKEN = "aio_Tpns72HEyXkIXko7394emsFLSZPL"
PORT = 1883
#  ---------------------------------------------------------------



# Adafruit feeds ------------------------------------------------------
feed = "dangnguyen/feeds/"
AIO_FEED_SUBCRIBE = [   "button1/",         # Fan controller
                        "button2/",         # Light controller
                        "button3/",         # Door controller
                        "FanValue/",        # Fan's rotation
                        "LightValue/",      # Light's brightness
                        #"sensor1/",         # temperature sensor
                        #"sensor2/",         # light sensor
                        "FanDisplay/",
                        "LightDisplay/"]    

AIO_FEED_PUBLISH = [   "button1/",         # Fan controller
                        "button2/",         # Light controller
                        "button3/",         # Door controller
                        "FanValue/",        # Fan's rotation
                        "LightValue/",      # Light's brightness
                        #"sensor1/",         # temperature sensor
                        #"sensor2/",         # light sensor
                        "FanDisplay/",
                        "LightDisplay/"]    

jsons = "json"
feedID = {
    "button1": 2463386,
    "button2": 2463387,
    "button3": 2494057,
    "FanValue": 2463415,
    "LightValue": 2465220,
    "sensor1": 2462542,
    "sensor2": 2464202,
    "LightDisplay" : 2470613,
    "FanDisplay" : 2470612
}
# ---------------------------------------------------------------------



# message received by serial ------------------------------------------
mess = ""
fanValue = ""
lightValue = ""
# ---------------------------------------------------------------------



# Get serial port =======================

'''
    @name: find_port()
    @param:
        None
    @exp:
        Find serial port connects to YOLO:bit.
'''
def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        if "USB Serial" in txt:
            return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

bbc_port = find_port()
if len(bbc_port) > 0:
    ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# =============================================================



# Basic MQTT functions defined by user =======================

def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    global fanValue, lightValue
    received =  json.loads(message.payload.decode("utf-8"))
    current_time = datetime.now().strftime("%d,%b.%H:%M:%S")
    cmd = "" 
    print("Received from: " + str(received['id']))
    #TODO: Update the cmd to control the device
    try:
        if received["id"] == feedID["FanValue"]:
            if received["last_value"] != "#":
                fanValue += received["last_value"]
                print(fanValue)
            else: 
                fanValue = fanValue.replace("*", "")
                
                if int(fanValue) >= 100:
                    fanValue = "100"
                # client.publish(feed + AIO_FEED_PUBLISH[6], int(fanValue))
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": int(fanValue)})
                cmd = "!FAN:ON:"+fanValue+"#"
        
        if received["id"] == feedID["LightValue"]:
            if received["last_value"] != "#":
                lightValue += received["last_value"]
                print(lightValue)
            else: 
                lightValue = lightValue.replace("*", "")
                
                if int(lightValue) >= 100:
                    lightValue = "100"
                # client.publish(feed + AIO_FEED_PUBLISH[7], int(lightValue))
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": int(lightValue)})
                cmd = "!LI:ON:"+lightValue+"#"

        if received["id"] == feedID["button1"]:
            if received["last_value"] == "ON":
                cmd = "!FAN:ON:0#"
                client.publish(feed + AIO_FEED_PUBLISH[6], int(40))
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": 40})
            if received["last_value"] == "OFF":
                cmd = "!FAN:OFF#"
                client.publish(feed + AIO_FEED_PUBLISH[6], int(0))
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "OFF", "value": 0})

        if received["id"] == feedID["FanDisplay"]:
            if int(received["last_value"]) > 0:
                cmd = "!FAN:ON:" + str(received["last_value"]) + "#"
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": int(received["last_value"])})
            if int(received["last_value"]) == 0:
                cmd = "!FAN:OFF#"
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "OFF", "value": 0})

        if received["id"] == feedID["button2"]:
            if received["last_value"] == "ON":
                cmd = "!LI:ON:0#"
                client.publish(feed + AIO_FEED_PUBLISH[7], int(40))
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": 40})
            if received["last_value"] == "OFF":
                cmd = "!LI:OFF#"
                client.publish(feed + AIO_FEED_PUBLISH[7], int(0))
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "OFF", "value": 0})
        
        if received["id"] == feedID["button3"]:
            if received["last_value"] == "ON":
                cmd = "!DO:ON#"
                Door_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON"})
            if received["last_value"] == "OFF":
                cmd = "!DO:OFF#"
                Door_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "OFF"})

        if received["id"] == feedID["LightDisplay"]:
            if int(received["last_value"]) > 0:
                cmd = "!LI:ON:" + str(received["last_value"]) + "#"
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "ON", "value": int(received["last_value"])})
            if int(received["last_value"]) == 0:
                cmd = "!LI:OFF#"
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": true, "status": "OFF", "value": 0})
# DEBUG ==========================================================
        # if received["id"] == feedID["sensor1"]:
        #     print("Temp: " + received["last_value"] + "°C")

        # if received["id"] == feedID["sensor2"]:
        #     print("Light: " + received["last_value"] + " lux")
# DEBUG ==========================================================
    except: 
        pass
    if len(bbc_port) > 0:
        ser.write(str(cmd).encode())


def connected(client, userdata, flags, rc):
        try:
            print("Connected successfully!!")
            for topic in AIO_FEED_SUBCRIBE:
                client.subscribe(feed+topic+jsons)
                print("Connected to " + topic + " successfully!!")
        except:
            print("Connection is failed")
            pass

# ===================================================



# Serial process ------------------------------------

'''
    @name: processData()
    @param:
        data: string
    @exp:
        from Serial, received data will be processed and pushed to Adafruit.
'''
def processData(data):
    print(data)
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    current_time = datetime.now().strftime("%d,%b.%H:%M:%S")
    if splitData[0] == "TE" and splitData[2] == "LI":
        # client.publish(feed + AIO_FEED_PUBLISH[0], float(splitData[1]))
        # client.publish(feed + AIO_FEED_PUBLISH[1], float(splitData[1]))
        sensor_collection.insert_one(
                {
                    "timestamp": f'{current_time}',     # time
                    "server_side": False,               # bool
                    "temp": float(splitData[1]),        
                    "light" : float(splitData[3])
                }
            )
        ser.write("!ACK:TELI#".encode())

    if splitData[0] == "BUT":
        if splitData[1] == "1":
            # client.publish(feed + AIO_FEED_PUBLISH[2], (splitData[2]))
            if splitData[2] == "ON":
                # client.publish(feed + AIO_FEED_PUBLISH[6], int(splitData[3]))
                fan_collection.insert_one(
                        {
                            "timestamp": f'{current_time}', 
                            "server_side": False, 
                            "status": "ON", 
                            "value": int(splitData[3])
                        }
                    )
            else: 
                # client.publish(feed + AIO_FEED_PUBLISH[6], 0)
                fan_collection.insert_one({"timestamp": f'{current_time}', "server_side": False, "status": "OFF", "value": 0})
            ser.write("!ACK:B1#".encode())

        if splitData[1] == "2":
            # client.publish(feed + AIO_FEED_PUBLISH[3], (splitData[2]))
            if splitData[2] == "ON":
                # client.publish(feed + AIO_FEED_PUBLISH[7], int(splitData[3]))
                Bulb_collection.insert_one(
                        {
                            "timestamp": f'{current_time}', 
                            "server_side": False, 
                            "status": "ON", 
                            "value": int(splitData[3])
                        }
                    )
            else: 
                # client.publish(feed + AIO_FEED_PUBLISH[7], 0)
                Bulb_collection.insert_one({"timestamp": f'{current_time}', "server_side": False, "status": "OFF", "value": 0})
            ser.write("!ACK:B2#".encode())

        if splitData[1] == "3":
            Door_collection.insert_one(
                    {
                        "timestamp": f'{current_time}', 
                        "server_side": False, 
                        "status": splitData[1]
                    }
                )
            ser.write("!ACK:B3#".encode())

'''
    @name: readSerial()
    @param:
        None
    @exp:
        Receiving data by readind byte to byte, and each message is between "!" and "#" characters.
'''
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

# --------------------------------------------------------------------



######################## PAHO-MQTT CONNECTION ########################
# define client
client = mqttclient.Client("Gateway_Adafruit")

# set username and password
client.username_pw_set(ADAFRUIT_USERNAME, ADAFRUIT_ACCESS_TOKEN)

# connect to broker with address and port
    # Port:
        # 1883: Insecure port.
        # 8883: Secure port.
        # 443: MQTT through Websocket. 
client.connect(BROKER_ADDRESS, 1883)


# subcribe and receive data from server. _________
client.on_connect = connected
client.loop_start()
client.on_subscribe = subscribed
client.on_message = recv_message
# ________________________________________________

######################## DONE ########################

'''
    Enter while loop.
'''
while True:

    if len(bbc_port) >  0:
        try:
            readSerial()
            
        except:
            pass

    time.sleep(1)
