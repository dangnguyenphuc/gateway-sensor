from event_manager import *
import sys
import uselect
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import time
from aiot_rgbled import RGBLed
from aiot_ir_receiver import *
from aiot_lcd1602 import LCD1602

# Mô tả hàm này...
def b3():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  b3_list = ''.join([str(x) for x in ['!', 'BUT:3:', door_status, '#']])

# Mô tả hàm này...
def b1():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  b1_list = ''.join([str(x2) for x2 in ['!', 'BUT:1:', fan_status, ':', fan_value, '#']])

# Mô tả hàm này...
def send_button1():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if ACK_b1_flag == 1:
    ACK_b1_flag = 0
    print(b1_list, end =' ')
    sendACK()
    b1_ack_time = timer.get()

# Mô tả hàm này...
def send_sensor_value():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if ACK_temp_li_flag == 1:
    ACK_temp_li_flag = 0
    sendACK()
    print(temp_light_list, end =' ')
    teli_ack_time = timer.get()

# Mô tả hàm này...
def b2():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  b2_list = ''.join([str(x3) for x3 in ['!', 'BUT:2:', light_status, ':', light_value, '#']])

# Mô tả hàm này...
def send_button2():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if ACK_b2_flag == 1:
    ACK_b2_flag = 0
    sendACK()
    print(b2_list, end =' ')
    b2_ack_time = timer.get()

event_manager.reset()

def read_terminal_input():
  spoll=uselect.poll()        # Set up an input polling object.
  spoll.register(sys.stdin, uselect.POLLIN)    # Register polling object.

  input = ''
  if spoll.poll(0):
    input = sys.stdin.read(1)

    while spoll.poll(0):
      input = input + sys.stdin.read(1)

  spoll.unregister(sys.stdin)
  return input

def on_event_timer_callback_d_t_W_A_C():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, fan_status, fan_value, light_status, light_value, lux, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, status, b3_list, door_status, ACK_b3_flag, b3_ack_time
  received_list = read_terminal_input()[1 : -1].split(':')
  cmd = received_list[0]
  if cmd == 'FAN':
    fan_status = received_list[1]
    if fan_status == 'ON':
      fan_value = int((received_list[2]))
      if fan_value == 0:
        fan_value = default_fan_value
        display.scroll('F1')
      else:
        display.scroll('F2')
      pin14.write_analog(round(translate(fan_value, 0, 100, 0, 1023)))
    else:
      fan_value = 0
      pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
  if cmd == 'LI':
    light_status = received_list[1]
    if light_status == 'ON':
      light_value = int((received_list[2]))
      if light_value == 0:
        light_value = default_light_value
        Light_on()
      else:
        Light_on()
    else:
      light_value = 0
      Light_on()
  if cmd == 'DO':
    door_status = received_list[1]
    Open_Door()
  if cmd == 'ACK':
    status = received_list[1]
    if status == 'TELI':
      ACK_temp_li_flag = 1
      temp_light_list = ''
    if status == 'B1':
      ACK_b1_flag = 1
      b1_list = ''
    if status == 'B2':
      ACK_b2_flag = 1
      b2_list = ''
    if status == 'B3':
      ACK_b3_flag = 1
      b3_list = ''
    receivedACK()

event_manager.add_timer_event(100, on_event_timer_callback_d_t_W_A_C)

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_g_e_s_y_K():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, fan_status, fan_value, light_status, light_value, lux, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, status, b3_list, door_status, ACK_b3_flag, b3_ack_time
  aiot_dht20.read_dht20()
  temp = aiot_dht20.dht20_temperature()
  lux = round(translate((pin2.read_analog()), 0, 4095, 0, 100))
  temp_light_list = ''.join([str(x4) for x4 in ['!', 'TE:', temp, ':', 'LI:', lux, '#']])
  send_sensor_value()

event_manager.add_timer_event(30000, on_event_timer_callback_g_e_s_y_K)

# Mô tả hàm này...
def receivedACK():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  display.show(Image("44044:04440:00400:40004:44044"))
  time.sleep_ms(100)
  display.show(Image("40004:44044:04440:00400:40004"))
  time.sleep_ms(100)
  display.show(Image("00400:40004:44044:04440:00400"))
  display.clear()

# Mô tả hàm này...
def sendACK():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  display.show(Image("01110:11011:10001:00100:01110"))
  time.sleep_ms(100)
  display.show(Image("11011:10001:00100:01110:11011"))
  time.sleep_ms(100)
  display.show(Image("10001:00100:01110:11011:10001"))
  display.clear()

def on_event_timer_callback_L_z_T_R_z():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, fan_status, fan_value, light_status, light_value, lux, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, status, b3_list, door_status, ACK_b3_flag, b3_ack_time
  if ACK_temp_li_flag == 0:
    if (timer.get()) - teli_ack_time >= 4000:
      ACK_temp_li_flag = 1
      send_sensor_value()
  if ACK_b1_flag == 0:
    if (timer.get()) - b1_ack_time >= 4000:
      ACK_b1_flag = 1
      send_button1()
  if ACK_b2_flag == 0:
    if (timer.get()) - b2_ack_time >= 4000:
      ACK_b2_flag = 1
      send_button2()
  if ACK_b3_flag == 0:
    if (timer.get()) - b3_ack_time >= 4000:
      ACK_b3_flag = 1
      send_button3()

event_manager.add_timer_event(2000, on_event_timer_callback_L_z_T_R_z)

# Mô tả hàm này...
def send_button3():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if ACK_b3_flag == 1:
    ACK_b3_flag = 0
    sendACK()
    print(b3_list, end =' ')
    b3_ack_time = timer.get()

tiny_rgb = RGBLed(pin0.pin, 4)

# Mô tả hàm này...
def Light_on():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if light_value > 0:
    tiny_rgb.show(1, hex_to_rgb('#ffffff'))
  elif light_value >= 40:
    tiny_rgb.show(2, hex_to_rgb('#ffffff'))
  elif light_value >= 70:
    tiny_rgb.show(3, hex_to_rgb('#ffffff'))
  elif light_value >= 100:
    tiny_rgb.show(4, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))

aiot_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); aiot_ir_rx.start();

def on_ir_receive_callback(t_C3_ADn_hi_E1_BB_87u, addr, ext):
  global b1_list, b2_list, received_list, default_fan_value, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, fan_status, fan_value, light_status, light_value, lux, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, status, b3_list, door_status, ACK_b3_flag, b3_ack_time
  if aiot_ir_rx.get_code() == IR_REMOTE_A:
    if fan_status == 'ON':
      fan_status = 'OFF'
      fan_value = 0
      pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
    else:
      fan_status = 'ON'
      fan_value = default_fan_value
      pin14.write_analog(round(translate(default_fan_value, 0, 100, 0, 1023)))
    b1()
    send_button1()
  if aiot_ir_rx.get_code() == IR_REMOTE_B:
    if light_status == 'ON':
      light_status = 'OFF'
      light_value = 0
    else:
      light_status = 'ON'
      light_value = default_light_value
    Light_on()
    b2()
    send_button2()
  if aiot_ir_rx.get_code() == IR_REMOTE_C:
    if door_status == 'ON':
      door_status = 'OFF'
    else:
      door_status = 'ON'
    Open_Door()
    b3()
    send_button3()
  if aiot_ir_rx.get_code() == IR_REMOTE_RIGHT:
    if fan_status == 'ON':
      fan_value = fan_value + 10
      if fan_value >= 100:
        fan_value = 100
      pin14.write_analog(round(translate(fan_value, 0, 100, 0, 1023)))
    b1()
    send_button1()
  if aiot_ir_rx.get_code() == IR_REMOTE_LEFT:
    if fan_status == 'ON':
      fan_value = fan_value - 10
      if fan_value <= 0:
        fan_status = 'OFF'
        fan_value = 0
      pin14.write_analog(round(translate(fan_value, 0, 100, 0, 1023)))
    b1()
    send_button1()
  if aiot_ir_rx.get_code() == IR_REMOTE_UP:
    if light_status == 'ON':
      light_value = light_value + 10
      if light_value >= 100:
        light_value = 100
      Light_on()
    b2()
    send_button2()
  if aiot_ir_rx.get_code() == IR_REMOTE_DOWN:
    if light_status == 'ON':
      light_value = light_value - 10
      if light_value <= 0:
        light_status = 'OFF'
        light_value = 0
      Light_on()
    b2()
    send_button2()
  aiot_ir_rx.clear_code()

aiot_ir_rx.on_received(on_ir_receive_callback)

aiot_lcd1602 = LCD1602()

def on_event_timer_callback_l_J_T_D_h():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, fan_status, fan_value, light_status, light_value, lux, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, status, b3_list, door_status, ACK_b3_flag, b3_ack_time
  aiot_lcd1602.clear()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('TE:')
  aiot_lcd1602.move_to(4, 0)
  aiot_lcd1602.putstr(temp)
  aiot_lcd1602.move_to(8, 0)
  aiot_lcd1602.putstr('F:')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr(fan_status)
  if fan_status != 'OFF':
    aiot_lcd1602.move_to(12, 0)
    aiot_lcd1602.putstr(fan_value)
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('LI:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(lux)
  aiot_lcd1602.move_to(8, 1)
  aiot_lcd1602.putstr('L:')
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr(light_status)
  if light_status != 'OFF':
    aiot_lcd1602.move_to(12, 1)
    aiot_lcd1602.putstr(light_value)

event_manager.add_timer_event(100, on_event_timer_callback_l_J_T_D_h)

# Mô tả hàm này...
def Open_Door():
  global t_C3_ADn_hi_E1_BB_87u, b1_list, b2_list, received_list, default_fan_value, b3_list, ACK_temp_li_flag, ACK_b1_flag, ACK_b2_flag, cmd, default_light_value, temp, ACK_b3_flag, fan_status, fan_value, light_status, light_value, lux, door_status, temp_light_list, teli_ack_time, b1_ack_time, b2_ack_time, b3_ack_time, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602, tiny_rgb
  if door_status == 'ON':
    pin0.servo_write(120)
  else:
    pin0.servo_write(0)

if True:
  default_fan_value = 40
  default_light_value = 50
  temp = aiot_dht20.dht20_temperature()
  lux = round(translate((pin2.read_analog()), 0, 4095, 0, 100))
  ACK_b1_flag = 1
  ACK_b2_flag = 1
  ACK_b3_flag = 1
  ACK_temp_li_flag = 1
  temp_light_list = ''.join([str(x5) for x5 in ['!', 'TE:', temp, 'LI:', lux, '#']])
  fan_status = 'OFF'
  light_status = 'OFF'
  door_status = 'OFF'
  fan_value = 0
  light_value = 0
  b1_list = ''.join([str(x6) for x6 in ['!', 'BUT:1:', fan_status, ':', fan_value, '#']])
  b2_list = ''.join([str(x7) for x7 in ['!', 'BUT:2:', light_status, ':', light_value, '#']])
  b3_list = ''.join([str(x8) for x8 in ['!', 'BUT:3:', door_status, '#']])
  teli_ack_time = 0
  b1_ack_time = 0
  b2_ack_time = 0
  b3_ack_time = 0
  timer.reset()
  display.clear()
  display.show(Image.SMILE)

while True:
  event_manager.run()
  time.sleep_ms(1000)
