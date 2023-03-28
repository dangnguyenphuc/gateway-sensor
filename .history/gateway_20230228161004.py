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
        if "USB Serial" in txt:
            return str(port).split("-")[0].strip()

mess = ""
bbc_port = find_port()

print("BBC PORT: " + bbc_port)

if len(bbc_port) > 0:
    ser = serial.Serial(port=bbc_port, baudrate=9600)


def connected(client):
    print("Connect Successfully ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe Successfully ...")

def disconnected(client):
    print("Disconnnected ...")
    sys.exit(1)

def message(client , feed_id , payload):
    print( "Received: " + payload)

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


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
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
