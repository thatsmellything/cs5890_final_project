## REQUIREMENTS
- `python3`
- `pip3`
- bash
## USAGE
- clone repository
- cd into repository
- run 'bash scan.sh' - this will scan bluetooth devices from interface 'hci0'
- to get device info run 'python3 bt_info.py target_mac'
- pick a device from the list that you wish to attack
- connect to the target device
- run 'python3 bt_ddos.py target_mac threads' - this will start the attack
- to stop the attack, press 'ctrl + c'
## SOLUTION DISCLAIMER
The solution proposed makes the l2ping requests happen every 1 second per thread. Thus redusing the overall bandwidth used by the attack. This is not a perfect solution, but is a starting point for development towards a hard ping request limit implemented into Bluetooth devices.

## DISCLAIMER
- I am not responsible for any damage done with this script

