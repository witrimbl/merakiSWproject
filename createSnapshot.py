
import os
import sys
import json
import meraki
from wireless import Wireless
from appliance import Appliance
from switch import Switch
from totalNetwork import TotalNetwork


baseURL = "https://api.meraki.com/api/v1"
API_KEY = 'exampleKey'  # first api key
apiKey = 'exampleKey'  # second api key

dashboard = meraki.DashboardAPI(
    api_key=API_KEY, base_url=baseURL, print_console=False)
organizations = dashboard.organizations.getOrganizations()
networks = dashboard.organizations.getOrganizationNetworks(
    organizations[0]['id'])
# print(json.dumps(networks, indent=2))
# you can choose to set these variables manually or if they are unknown you can use the api calls above
# to find them then set the index ([0]) that coresponds to the wanted network and orginization
networkID = networks[0]['id']
orgID = organizations[0]['id']


# Retrieve list of devices
devices = dashboard.networks.getNetworkDevices(networkID)
numDevices = len(devices)
# print(json.dumps(devices, indent=2))

snapshot = {}
# Gather config snapshot of each device
for i in range(numDevices):
    deviceInfo = devices[i]
    deviceType = deviceInfo['model'][0:2]
    # Call appropriate function depending on device type
    if deviceType == "MR":
        device = Wireless(deviceInfo['serial'], networkID, apiKey)
        identifier = "MR:" + deviceInfo['serial']
        snapshot[identifier] = device.collectInfo()
    elif deviceType == "MS":
        device = Switch(deviceInfo['serial'], networkID, apiKey)
        identifier = "MS:" + deviceInfo['serial']
        snapshot[identifier] = device.collectInfo()
    elif deviceType == "MX":
        device = Appliance(deviceInfo['serial'], networkID, orgID, apiKey)
        identifier = "MX:" + deviceInfo['serial']
        snapshot[identifier] = device.collectInfo()


device = TotalNetwork(networkID, apiKey)
identifier = "Network"
#snapshot = {}
snapshot[identifier] = device.collectInfo()


with open("snapshot.json", "w") as outfile:
    json.dump(snapshot, outfile, indent=2)

# end of create snapshot code
