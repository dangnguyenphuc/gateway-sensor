# import sys
# from Adafruit_IO import MQTTClient
# import serial.tools.list_ports
# import time
# import random

# AIO_FEED_ID = ["button1", "button2"]
# AIO_USERNAME = "dangnguyen"
# AIO_KEY = "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn"

# def find_port():
#     for port in list(serial.tools.list_ports.comports()):
#         txt = str(port)
#         if "USB Serial" in txt:
#             return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

# mess = ""
# bbc_port = find_port()

# print("BBC PORT: " + bbc_port)

# if len(bbc_port) > 0:
#     ser = serial.Serial(port=bbc_port, baudrate=9600)
#     print("Connected")

# def serialWrite(msg):
#     ser.write(str(msg).encode())

# def connected(client):
#     print("Connect Successfully ...")
#     for topic in AIO_FEED_ID:
#         client.subscribe(topic)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe Successfully ...")

# def disconnected(client):
#     print("Disconnnected ...")
#     sys.exit(1)

# def received(client , feed_id , payload):
#     print( "Received feed_id "+ str(feed_id) +": " + payload)
#     # cmd = ""
#     # if feed_id == "button1":
#     #     if str(payload) == "ON":
#     #         cmd = ""


#     # if feed_id == "button2":


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
# client.on_message = received
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


import serial, sys
def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        if "USB Serial" in txt:
            return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()
port = your_port_name
baudrate = 9600
ser = serial.Serial(port,baudrate,timeout=0.001)
while True:
    data = ser.read(1)
    data+= ser.read(ser.inWaiting())
    sys.stdout.write(data)
    sys.stdout.flush()
