from colorama import Fore
from os import system
from time import sleep
import socket
print("")
print(Fore.LIGHTCYAN_EX+"/START....")
sleep(2)
system("clear")
print(Fore.LIGHTRED_EX+"["+Fore.LIGHTGREEN_EX+"/start"+Fore.LIGHTRED_EX+"]")
sleep(1)
print()
print(Fore.LIGHTRED_EX+"["+Fore.LIGHTGREEN_EX+"MR-DARK"+Fore.LIGHTRED_EX+"]")
sleep(1)
print()
print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTRED_EX+"D.A.R.K"+Fore.LIGHTGREEN_EX+"]")
sleep(1)
print()
print(Fore.LIGHTBLUE_EX+""".-.-..
          /+/++//
         /+/++//
  *   * /+/++//
   \ /  |/__//
 {X}v{X}|WEB|==========.
   (')  /'|'\           \
       /  \  \          '
       \_  \_ \_   ___DARK 1.0___""")
print()
def MR():
  print(Fore.LIGHTCYAN_EX+"My coding: "+Fore.LIGHTYELLOW_EX+"MR-DARK")
  print(Fore.LIGHTCYAN_EX+"My chaneel: "+Fore.LIGHTYELLOW_EX+"https://t.me/Cyber_Seven")
  print(Fore.LIGHTCYAN_EX+"Version: "+Fore.LIGHTYELLOW_EX+"1.0")
  print()
  site = input(Fore.LIGHTRED_EX+"Enter Target (Defalte: filimo.com): "+Fore.LIGHTGREEN_EX)
  sleep(2)
  print("")
  print(Fore.LIGHTMAGENTA_EX+"HACK WEBSITE:"+Fore.LIGHTGREEN_EX)
  print("")
  site = site.replace("https://","")
  site = site.replace("http://","")
  site = site.replace("www.","")
  
  if site[-3:] == "org":
    server = "whois.internic.net"
  else:
    server = "whois.iana.org"
    
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((server,43))
  s.send((site+"\r\n").encode())
  
  msg = s.recv(10000)
  print(msg.decode())
MR()