###################################### MacOS, Chrome 98. ######################################
print("Hello ThingsBoard")
import paho.mqtt.client as mqttclient
import json
import time
import serial.tools.list_ports
import re
from threading import Thread


def find_port():
    for port in list(serial.tools.list_ports.comports()):
        txt = str(port)
        if "USB Serial" in txt:
            return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

mess = ""
global status
bbc_port = find_port()
print(bbc_port)
if len(bbc_port) > 0:
    ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
    print(ser)

def processData(data):
    print(data)
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)

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

while True:

    if len(bbc_port) >  0:
        try:
            readSerial()
            ser.write("!FAN#".encode())
            print("DONE")
        except:
            pass
    
    time.sleep(4)

    if len(bbc_port) >  0:
        try:
            readSerial()
            ser.write("!LI#".encode())
            print("DONE")
        except:
            pass
    time.sleep(4)