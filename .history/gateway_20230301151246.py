import sys
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import time
import random

AIO_FEED_ID = [""]
AIO_USERNAME = "dangnguyen"
AIO_KEY = "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn"

def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        # if "USB Serial" in txt:
        #     return str(port).split("-")[0].strip()
        print(port)

# mess = ""
# bbc_port = find_port()

# print("BBC PORT: " + bbc_port)

# if len(bbc_port) > 0:
#     ser = serial.Serial(port=bbc_port, baudrate=9600)


# def connected(client):
#     print("Connect Successfully ...")
#     for topic in AIO_FEED_ID:
#         client.subscribe(topic)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe Successfully ...")

# def disconnected(client):
#     print("Disconnnected ...")
#     sys.exit(1)

# def message(client , feed_id , payload):
#     print( "Received: " + payload)

# def processData(data):

#     data = data.replace("!", "")
#     data = data.replace("#", "")
#     splitData = data.split(":")
#     print(splitData)
#     #TODO: Add your source code to publish data to the server
#     if splitData[0] == 'TEMP':
#         temp = splitData[1]
#         client.publish('sensor1', temp)

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


# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()

# # timer = 2


# while True:    
#     if len(bbc_port) >  0:
#         try:
#             readSerial()
#         except:
#             pass
#     time.sleep(1)
