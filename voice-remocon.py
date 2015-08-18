# -*- coding: utf-8 -*-

import socket
import sys
import select
import os
import threading

host = "localhost"
port = 10500
bufsize = 1024
timer_length = 20.0
standby = False
    
os.system("gpio -g mode 8 out")
os.system("gpio -g mode 7 out")
os.system("gpio -g mode 23 out")
os.system("gpio -g mode 24 out")

os.system("/home/pi/jtalk.sh 音声リモコンを起動しました")  

def standbyOff():
    global standby
    if standby == True:
        os.system("/home/pi/jtalk.sh 命令待機モードを自動解除します")
        standby = False
        os.system("gpio -g write 8 0")
        os.system("gpio -g write 7 0")
        os.system("gpio -g write 23 0")
        os.system("gpio -g write 24 0")
        
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:

  inputready, outputready, exceptrdy = select.select([client_socket], [],[])

  for s in inputready:
    if s == client_socket:
        message = client_socket.recv(bufsize)
        print "受信したメッセージ : " + message
        if message == "":
            print "クライアントの実行を停止します"
            break
        if standby == True:
            if "前進" in message:
                os.system("gpio -g write 8 1")
                os.system("gpio -g write 7 0")
                os.system("gpio -g write 23 1")
                os.system("gpio -g write 24 0")
            if "後進" in message:
                os.system("gpio -g write 8 0")
                os.system("gpio -g write 7 1")
                os.system("gpio -g write 23 0")
                os.system("gpio -g write 24 1")
            if "停止" in message:
                os.system("gpio -g write 8 0")
                os.system("gpio -g write 7 0")
                os.system("gpio -g write 23 0")
                os.system("gpio -g write 24 0")
            if "右前" in message:
                os.system("gpio -g write 8 1")
                os.system("gpio -g write 7 0")
                os.system("gpio -g write 23 0")
                os.system("gpio -g write 24 0")
            if "左前" in message:
                os.system("gpio -g write 8 0")
                os.system("gpio -g write 7 0")
                os.system("gpio -g write 23 1")
                os.system("gpio -g write 24 0")
            if "右後" in message:
                os.system("gpio -g write 8 0")
                os.system("gpio -g write 7 1")
                os.system("gpio -g write 23 0")
                os.system("gpio -g write 24 0")
            if "左後" in message:
                os.system("gpio -g write 8 0")
                os.system("gpio -g write 7 0")
                os.system("gpio -g write 23 0")
                os.system("gpio -g write 24 1")
            if "命令受付モードOFF" in message:
                standby = False
                os.system("/home/pi/jtalk.sh 命令待機モードを強制解除します")
            if "命令受付モードON" in message:
                os.system("/home/pi/jtalk.sh 既に命令待機中です")
        elif "命令受付モードON" in message:
            os.system("/home/pi/jtalk.sh 命令待機モードに入ります")
            standby = True
            t = threading.Timer(timer_length, standbyOff)
            t.start()
        
client_socket.close()

