import os


hostname = ' www.cisco.com '
response = os.system("ping -c 3" + hostname)
if response == 0 :
    print(hostname + ' is reachable. ')
else:
    print(hostname + ' is not reachable. ')

