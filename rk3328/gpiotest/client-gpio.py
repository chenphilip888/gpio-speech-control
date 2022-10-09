#!/usr/bin/python3

import socket
import time
import speech_recognition as sr

HOST = '192.168.86.50'   # The remote host
PORT = 50007              # The same port as used by the server

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

r = sr.Recognizer()
r.energy_threshold = 1568
r.dynamic_energy_threshold = True
bye = 0

while bye == 0:
   with sr.Microphone(sample_rate=44100) as source:
       # r.adjust_for_ambient_noise(source)
       print ("Start Listening...")
       audio = r.listen(source, phrase_time_limit = 4)
       cmd = r.recognize_google(audio)
   
   print ("Done Listening...")
   try:
       print("You said " + cmd)
       if cmd == "begin test":
           sock.sendall("start".encode())
           print(sock.recv(1024))
       elif cmd == "turn on the light":
           sock.sendall("led_on".encode())
           print(sock.recv(1024))
       elif cmd == "turn off the light":
           sock.sendall("led_off".encode())
           print(sock.recv(1024))
       elif cmd == "Red Cross":
           sock.sendall("lcd_red".encode())
           print(sock.recv(1024))
       elif cmd == "green grass":
           sock.sendall("lcd_green".encode())
           print(sock.recv(1024))
       elif cmd == "sky is blue":
           sock.sendall("lcd_blue".encode())
           print(sock.recv(1024))
       elif cmd == "Yellow River":
           sock.sendall("lcd_yellow".encode())
           print(sock.recv(1024))
       elif cmd == "cyan color":
           sock.sendall("lcd_cyan".encode())
           print(sock.recv(1024))
       elif cmd == "purple mountain":
           sock.sendall("lcd_purple".encode())
           print(sock.recv(1024))
       elif cmd == "White House":
           sock.sendall("lcd_white".encode())
           print(sock.recv(1024))
       elif cmd == "blackjack":
           sock.sendall("lcd_black".encode())
           print(sock.recv(1024))
       elif cmd == "stay in the middle":
           sock.sendall("servo_middle".encode())
           print(sock.recv(1024))
       elif cmd == "turn right":
           sock.sendall("servo_right".encode())
           print(sock.recv(1024))
       elif cmd == "turn left":
           sock.sendall("servo_left".encode())
           print(sock.recv(1024))
       elif cmd == "stop":
           sock.sendall("servo_stop".encode())
           print(sock.recv(1024))
           sock.sendall("bye".encode())
           print(sock.recv(1024))
           sock.close()
           bye = 1
   
   except sr.UnknownValueError:
       print("Oops! Didn't catch that")
   except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))
