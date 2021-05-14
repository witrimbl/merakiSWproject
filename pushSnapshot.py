
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
apiKey = 'exampleKey'  # second API key

dashboard = meraki.DashboardAPI(
    api_key=API_KEY, base_url=baseURL, print_console=False)
organizations = dashboard.organizations.getOrganizations()
networks = dashboard.organizations.getOrganizationNetworks(
    organizations[0]['id'])
networkID = networks[0]['id']
orgID = organizations[0]['id']

data = {}

with open('snapshot.json') as json_file:
    data = json.load(json_file)


for device in data:
    ss = data[device]
    deviceType = device[0:2]
    serial = device[3:]
    if deviceType == "MR":
        device = Wireless(serial, networkID, apiKey, ss)
        device.pushInfo()
    elif deviceType == "MS":
        device = Switch(serial, networkID, apiKey, ss)
        device.pushInfo()
    elif deviceType == "MX":
        device = Appliance(serial, networkID, orgID, apiKey, ss)
        device.pushInfo()
    else:
        dev = TotalNetwork(networkID, apiKey, ss)
        dev.pushInfo()

# end of push code
