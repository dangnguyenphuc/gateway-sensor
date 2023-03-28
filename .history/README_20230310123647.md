# GATEWAY AND PROCESSOR FOR MULTIDISCIPLINARY PROJECT
* Ho Chi Minh University of Technology.
* __[CO3107] [L09]__
* Group: NMDK
    - Nguyễn Đoàn Nhật Minh -- 2010416
    - Vũ Đăng Khoa -- 2011436 
    - Nguyễn Nhựt Nguyên -- 2011706 
    - Nguyễn Phúc Đăng -- 2012968
* Author: Nguyen Phuc Dang.

## Abstract
In this project, we will implement a smart home system using YOLO:bit as a main node to collect data, local computer as a gateway to communication with [__`adafruit.io`__](https://io.adafruit.com/).

## Update

### v.1.0
* Gateway and YOLO:bit are serial connected.
* Gateway: 
    + Communication and get data from server.
![GATEWAY - Received data from Server](img/v.1.0/gateway_receive.png)
    + Push data to server.

* YOLO:bit: Receiving and sending data to gateway.
    - YOLO:bit Pins:

        + P0: Light.
        + P1: Light sensor.
        + P14,15: Fan.
        + P19,20 (I2C_1): DHT20 sensor.
        + P19,20 (I2C_2): LCD1602.
    - General: 
    ![](img/v.1.0/yolo%3Abit_general.png)
### v.1.1
* Gateway: Correct some wrong syntax.

### v.1.1
* Gateway: Add local database to store sensors data.