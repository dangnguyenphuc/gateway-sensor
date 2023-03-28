from event_manager import *
import sys
import uselect
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
from aiot_lcd1602 import LCD1602
from aiot_ir_receiver import *

event_manager.reset()

def on_event_timer_callback_J_O_C_n_V():
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, t_C3_ADn_hi_E1_BB_87u, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  b1_list[-1] = ''.join([str(x) for x in ['!', 'BUT:1:', fan_status, '#']])
  b2_list[-1] = ''.join([str(x2) for x2 in ['!', 'BUT:2:', light_status, '#']])
  if ACK_b1_flag == 1:
    ACK_b1_flag = 0
    sendACK()
    print((b1_list[0]), end =' ')
  if ACK_b2_flag == 1:
    ACK_b2_flag = 0
    sendACK()
    print((b2_list[0]), end =' ')

event_manager.add_timer_event(1000, on_event_timer_callback_J_O_C_n_V)

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
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, t_C3_ADn_hi_E1_BB_87u, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  received_list = read_terminal_input()[1 : -1].split(':')
  if not not len(received_list):
    cmd = received_list[0]
    display.show(cmd)
    if cmd == 'FAN':
      fan_status = received_list[1]
      if fan_status == 'ON':
        value = received_list[2]
        pin14.write_digital((1))
        display.show(Image.HEART)
        if (int(value)) == 0:
          pin14.write_analog(round(translate(default_fan_value, 0, 100, 0, 1023)))
          display.scroll('F1')
        else:
          pin14.write_analog(round(translate((int(value)), 0, 100, 0, 1023)))
          display.scroll('F2')
      if fan_status == 'OFF':
        display.show(Image.FABULOUS)
        pin14.write_analog(round(translate(0, 0, 100, 0, 1023)))
        pin15.write_digital((0))
        pin14.write_digital((0))
    if cmd == 'LI':
      light_status = received_list[1]
      if light_status == 'ON':
        value = received_list[2]
        display.show(Image.HEART_SMALL)
        if (int(value)) == 0:
          display.scroll('L1')
          pin0.write_digital(1)
          pin0.write_analog(round(50*10.23))
        else:
          display.scroll('L2')
          pin0.write_digital(1)
          pin0.write_analog(round((int(value))*10.23))
      if light_status == 'OFF':
        pin0.write_digital(0)
        display.show(Image.CONFUSED)
        pin0.write_digital((0))
    if cmd == 'ACK':
      status = received_list[1]
      if status == 'TE':
        ACK_temp_flag = 1
        temp_list = temp_list[1 : ]
      if status == 'LI':
        ACK_light_flag = 1
        light_list = light_list[1 : ]
      if status == 'B1':
        ACK_b1_flag = 1
        b1_list = b1_list[1 : ]
      if status == 'B2':
        ACK_b2_flag = 1
        b2_list = b2_list[1 : ]
      receivedACK()

event_manager.add_timer_event(100, on_event_timer_callback_d_t_W_A_C)

# Mô tả hàm này...
def receivedACK():
  global t_C3_ADn_hi_E1_BB_87u, default_fan_value, received_list, default_light_value, ACK_temp_flag, temp, b1_list, cmd, ACK_light_flag, lux, b2_list, fan_status, light_status, ACK_b1_flag, temp_list, ACK_b2_flag, light_list, value, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602
  display.show(Image("44044:04440:40404:44044:04440"))
  time.sleep_ms(100)
  display.show(Image("40404:44044:04440:40404:44044"))
  time.sleep_ms(100)
  display.show(Image("04440:40404:44044:04440:40404"))

# Mô tả hàm này...
def sendACK():
  global t_C3_ADn_hi_E1_BB_87u, default_fan_value, received_list, default_light_value, ACK_temp_flag, temp, b1_list, cmd, ACK_light_flag, lux, b2_list, fan_status, light_status, ACK_b1_flag, temp_list, ACK_b2_flag, light_list, value, status, aiot_ir_rx, aiot_dht20, aiot_lcd1602
  display.show(Image("01110:11011:10101:01110:11011"))
  time.sleep_ms(100)
  display.show(Image("11011:10101:01110:11011:10101"))
  time.sleep_ms(100)
  display.show(Image("10101:01110:11011:10101:01110"))

def on_event_timer_callback_g_e_s_y_K():
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, t_C3_ADn_hi_E1_BB_87u, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  if ACK_temp_flag == 1:
    ACK_temp_flag = 0
    sendACK()
    print((temp_list[0]), end =' ')
  if ACK_light_flag == 1:
    ACK_light_flag = 0
    sendACK()
    print((light_list[0]), end =' ')

event_manager.add_timer_event(5000, on_event_timer_callback_g_e_s_y_K)

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_S_p_b_k_s():
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, t_C3_ADn_hi_E1_BB_87u, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  aiot_dht20.read_dht20()
  temp = aiot_dht20.dht20_temperature()
  lux = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
  temp_list[-1] = ''.join([str(x3) for x3 in ['!', 'TE:', temp, '#']])
  light_list[-1] = ''.join([str(x4) for x4 in ['!', 'LI:', lux, '#']])

event_manager.add_timer_event(4500, on_event_timer_callback_S_p_b_k_s)

aiot_lcd1602 = LCD1602()

def on_event_timer_callback_l_J_T_D_h():
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, t_C3_ADn_hi_E1_BB_87u, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('TEMP:')
  aiot_lcd1602.move_to(7, 0)
  aiot_lcd1602.putstr(temp)
  aiot_lcd1602.move_to(11, 0)
  aiot_lcd1602.putstr('C')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('LUX: ')
  aiot_lcd1602.move_to(7, 1)
  aiot_lcd1602.putstr(lux)
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr('lux')

event_manager.add_timer_event(100, on_event_timer_callback_l_J_T_D_h)

aiot_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); aiot_ir_rx.start();

def on_ir_receive_callback(t_C3_ADn_hi_E1_BB_87u, addr, ext):
  global default_fan_value, received_list, temp, cmd, ACK_temp_flag, lux, status, ACK_light_flag, temp_list, light_list, value, http_response, default_light_value, list2, fan_status, light_status, ACK_b1_flag, ACK_b2_flag, b1_list, b2_list
  if False:
    pass
  aiot_ir_rx.clear_code()

aiot_ir_rx.on_received(on_ir_receive_callback)

if True:
  default_fan_value = 40
  default_light_value = 40
  temp = 0
  lux = 0
  ACK_b1_flag = 1
  ACK_b2_flag = 1
  ACK_temp_flag = 1
  ACK_light_flag = 1
  temp_list = []
  light_list = []
  b1_list = []
  b2_list = []
  fan_status = 'OFF'
  light_status = 'OFF'
  display.clear()
  display.show(Image.SMILE)

while True:
  event_manager.run()
  time.sleep_ms(1000)
