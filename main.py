import time
from time import sleep
from os import system
import socket    
import requests,re,os
from platform import platform
from subprocess import call
import os

puk = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'
    

print("""$$$$$$\ $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$\       $$\        $$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\   $$\ 
\_$$  _|$$$\  $$ |$$  __$$\\__$$  __| $$  __$$\ $$ |      $$ |      $$  __$$\\__$$  __|\_$$  _| $$  __$$\ $$$\  $$ |
  $$ |  $$$$\ $$ |$$ /  \__|  $$ |   $$ /  $$ |$$ |      $$ |      $$ /  $$ |  $$ |     $$ |  $$ /  $$ |$$$$\ $$ |
  $$ |  $$ $$\$$ |\$$$$$$\    $$ |   $$$$$$$$ |$$ |      $$ |      $$$$$$$$ |  $$ |     $$ |  $$ |  $$ |$$ $$\$$ |
  $$ |  $$ \$$$$ | \____$$\   $$ |   $$  __$$ |$$ |      $$ |      $$  __$$ |  $$ |     $$ |  $$ |  $$ |$$ \$$$$ |
  $$ |  $$ |\$$$ |$$\   $$ |  $$ |   $$ |  $$ |$$ |      $$ |      $$ |  $$ |  $$ |     $$ |  $$ |  $$ |$$ |\$$$ |
$$$$$$\ $$ | \$$ |\$$$$$$  |  $$ |   $$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |  $$ |   $$$$$$\  $$$$$$  |$$ | \$$ |
\______|\__|  \__| \______/   \__|   \__|  \__|\________|\________|\__|  \__|  \__|   \______| \______/ \__|  \__|
                                                                                                                  
                                                                                                                  
                                                                                                                  
""")
print("Install?")
time.sleep(0.5)
print("yes / no")

choice = input("")

if choice == "yes":
    time.sleep(0.05)
    print("""                  _   _ _ 
                 | | (_) |
  _ __  ___ _   _| |_ _| |
 | '_ \/ __| | | | __| | |
 | |_) \__ \ |_| | |_| | |
 | .__/|___/\__,_|\__|_|_|
 | |                      
 |_|                      
    """)
    os.system('pip3 install psutil')
    time.sleep(0.1)
    os.system(delet)
    
    print("""                    _   _ _ 
                   | | (_) |
   __ _ _ __  _   _| |_ _| |
  / _` | '_ \| | | | __| | |
 | (_| | |_) | |_| | |_| | |
  \__, | .__/ \__,_|\__|_|_|
   __/ | |                  
  |___/|_|                  
    """)
    os.system('pip3 install gputil')
    time.sleep(0.1)
    os.system(delet)
    
    print("""  _        _           _       _       
 | |      | |         | |     | |      
 | |_ __ _| |__  _   _| | __ _| |_ ___ 
 | __/ _` | '_ \| | | | |/ _` | __/ _ \
 | || (_| | |_) | |_| | | (_| | ||  __/
  \__\__,_|_.__/ \__,_|_|\__,_|\__\___|
                                       
                                       
    """)
    os.system('pip3 install tabulate')
    time.sleep(0.1)
    os.system(delet)
    
    print("""                        _                              _           
                       | |                            | |          
   ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
  / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
 | (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
  \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
             __/ | |              __/ |         | |           __/ |
            |___/|_|             |___/          |_|          |___/ 
    """)
    os.system('pip3 install cryptography')
    time.sleep(0.1)
    os.system(delet)
    
    print("""                        ____                             
     /\                / __ \                            
    /  \   _ __  _ __ | |  | |_ __   ___ _ __   ___ _ __ 
   / /\ \ | '_ \| '_ \| |  | | '_ \ / _ \ '_ \ / _ \ '__|
  / ____ \| |_) | |_) | |__| | |_) |  __/ | | |  __/ |   
 /_/    \_\ .__/| .__/ \____/| .__/ \___|_| |_|\___|_|   
          | |   | |          | |                         
          |_|   |_|          |_|                         
    """)
    os.system('pip install AppOpener')
    time.sleep(0.1)
    os.system(delet)
    
    time.sleep(2)
    print("Running script in about 10 Secounds")
    time.sleep(10)
    call(["python", "LMAO.py"])



if choice == "no":
    call(["python", "fail.py"])
    
