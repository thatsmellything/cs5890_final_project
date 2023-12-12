# Description: This script will scan for bluetooth device and ask to list the services they 
# provide.

import os
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python3 %s <mac>" % argv[0])
        exit()
    array = []
    target = argv[1]
    

    #parse target input so that ATTACK() can be called with the mac address
    array.append(target)
    target_final = str(array)
    target_final = target_final.replace("[", "")
    target_final = target_final.replace("]", "")
    target_final = target_final.replace("'", "")
    target_final = target_final.replace(" ", "")

    print("Target: " + target_final)
    
    os.system("sdptool browse " + str(target_final))


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