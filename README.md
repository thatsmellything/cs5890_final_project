## REQUIREMENTS
- `python3`
- `pip3`
- 'bash'
## USAGE
- clone repository
- cd into repository
- run `bash scan.sh` - this will scan bluetooth devices from interface 'hci0'
- to get device info run 'python3 bt_info.py <mac>'
- pick a device from the list that you wish to attack
- connect to the target device
- run 'python3 bt_ddos.py <mac> <threads>' - this will start the attack
- to stop the attack, press 'ctrl + c'

## DISCLAIMER
- I am not responsible for any damage done with this script

