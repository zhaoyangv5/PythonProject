import json

with open('switches.json') as f:
    devices = json.load(f)
    print(devices)
    for device in devices:
        # print(device['name'])
        print(device['connection']['host'])