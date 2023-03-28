import sys
from Adafruit_IO import MQTTClient
import serial.tools.list_ports
import time
import random

AIO_FEED_ID = ["button1", "button2","FanValue"]
AIO_USERNAME = "dangnguyen"
AIO_KEY = "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn"
cmd = ""
mess = ""

def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        if "USB Serial" in txt:
            return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

bbc_port = find_port()

if len(bbc_port) > 0:
    ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
    print(ser)

def serialWrite(msg):
    ser.write(str(msg).encode())

def connected(client):
    print("Connect Successfully ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe Successfully ...")

def disconnected(client):
    print("Disconnnected ...")
    sys.exit(1)

def received(client , feed_id , payload):
    global cmd
    print( "Received feed_id "+ str(feed_id) +": " + payload)
    try:
        if feed_id == "FanValue":
            if payload != "#":
                cmd += payload
                print(cmd)
            else: 
                cmd = cmd.replace("*", "")
                cmd = "!FAN:ON:"+cmd+"#"
                print("Send: " + cmd)
                serialWrite(cmd)
        if feed_id == "button1":
            if str(payload) == "ON":
                cmd = "!FAN:ON:0#"
                print("Send: " + cmd)
                serialWrite(cmd)
            if str(payload) == "OFF":
                cmd = "!FAN:OFF#"
                print("Send: " + cmd)
                serialWrite(cmd)
    except: 
        pass
    

def processData(client, data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)

    if splitData[0] == "TEMP":
        client.publish("sensor1", splitData[1])
        serialWrite("!ACK:TE#")
    if splitData[0] == "LUX":
        client.publish("sensor2", splitData[1])
        serialWrite("!ACK:LI#")
    

def readSerial(client):
    bytesToRead = ser.inWaiting()
    print(bytesToRead)
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(client,mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = received
client.on_subscribe = subscribe
client.connect()
client.loop_background()

# timer = 2


while True:    
    if len(bbc_port) >  0:
        try:
            readSerial()
        except:
             pass
    time.sleep(1)
    



