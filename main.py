import threading 
import socket
import sys
import time
import platform  
from djitellopy import Tello

host = ''
port = 9000
locaddr = (host,port) 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

Tello.takeoff()
Tello.move_forward(100)
Tello.rotate_clockwise(90)
Tello.move_forward(100)
Tello.rotate_clockwise(90)
Tello.move_forward(100)
Tello.rotate_clockwise(90)
Tello.move_forward(100)
Tello.rotate_clockwise(90)
Tello.land()
