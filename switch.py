import meraki
import json
import requests


class Switch:
    def __init__(self, serial, networkID, apiKey, dictionary={}):
        self.device = "Switch"
        self.serial = serial
        self.networkID = networkID
        # input second API key from dashboard into the variable below (meraki.DashboardAPI(api_key=xxxxxx))
        self.dashboard = meraki.DashboardAPI(
            api_key='exampleKey', base_url='https://api.meraki.com/api/v1', print_console=False)
        self.snapshot = dictionary
        self.apiKey = apiKey
    # GET
    # gets all device switchports

    def getDeviceSwitchPorts(self):
        try:
            response = self.dashboard.switch.getDeviceSwitchPorts(self.serial)
            self.snapshot['DeviceSwitchPorts'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # Returns l3 routing interfaces on switch

    def getDeviceSwitchRoutingInterfaces(self):
        try:
            response = self.dashboard.switch.getDeviceSwitchRoutingInterfaces(
                self.serial)
            self.snapshot['DeviceSwitchRoutingInterfaces'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # returns dhcp information for routing interfaces on switch

    def getDeviceSwitchRoutingInterfaceDhcp(self):
        try:
            interfaces = self.dashboard.switch.getDeviceSwitchRoutingInterfaces(
                self.serial)
            dhcpDict = {}
            for i in interfaces:
                response = self.dashboard.switch.getDeviceSwitchRoutingInterfaceDhcp(
                    self.serial, i['interfaceId'])
                dhcpDict[i['interfaceId']] = response
            self.snapshot['DeviceSwitchRoutingInterfaceDhcp'] = dhcpDict
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # returns configured static routes

    def getDeviceSwitchRoutingStaticRoutes(self):
        try:
            response = self.dashboard.switch.getDeviceSwitchRoutingStaticRoutes(
                self.serial)
            self.snapshot['DeviceSwitchRoutingStaticRoutes'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # returns warm spare information for switch

    def getDeviceSwitchWarmSpare(self):
        try:
            response = self.dashboard.switch.getDeviceSwitchWarmSpare(
                self.serial)
            self.snapshot['DeviceSwitchWarmSpare'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # PUT
    # pushes switchport information to dashboard from snapshot

    def putDeviceSwitchPorts(self):
        try:
            ports = self.snapshot['DeviceSwitchPorts']
            for p in ports:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/ports/{p['portId']}"
                payload = json.dumps(p)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # pushes warm spare information to dashboard from snapshot

    def putDeviceSwitchWarmSpare(self):
        try:
            url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/warmSpare"
            payload = json.dumps(self.snapshot['DeviceSwitchWarmSpare'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apiKey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # DELETE
    # Deletes routing interface dhcp information for switches on network
    def delDeviceSwitchRoutingInterfaceDhcp(self):
        try:
            interfaces = self.dashboard.switch.getDeviceSwitchRoutingInterfaces(
                self.serial)
            for i in interfaces:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/interfaces/{i['interfaceId']}/dhcp"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # deletes routing interface information for switches on network

    def delDeviceSwitchRoutingInterface(self):
        try:
            interfaces = self.dashboard.switch.getDeviceSwitchRoutingInterfaces(
                self.serial)
            for i in interfaces:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/interfaces/{i['interfaceId']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # deletes static route informatoin on switches

    def delDeviceSwitchRoutingStaticRoute(self):
        try:
            routes = self.dashboard.switch.getDeviceSwitchRoutingStaticRoutes(
                self.serial)
            for r in routes:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/staticRoutes/{r['staticRouteId']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # CREATE
    # pushes routing interface information to dashboard from snapshot

    def postDeviceSwitchRoutingInterfaces(self):
        try:
            interfaces = self.snapshot['DeviceSwitchRoutingInterfaces']
            for i in interfaces:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/interfaces"
                payload = json.dumps(i)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # pushes routining interface dhcp information to dashboard from snapshot

    def postDeviceSwitchRoutingInterfaceDhcp(self):
        try:
            interfaces = self.snapshot['DeviceSwitchRoutingInterfaceDhcp']
            for i in interfaces:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/interfaces/{i['interfaceId']}"
                payload = json.dumps(i)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # pushes static route infomration to dashboard from snapshot

    def postDeviceSwitchRoutingStaticRoutes(self):
        try:
            routes = self.snapshot['DeviceSwitchRoutingStaticRoutes']
            for r in routes:
                url = f"https://api.meraki.com/api/v1/devices/{self.serial}/switch/routing/staticRoutes/"
                payload = json.dumps(r)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apiKey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # defines all get calls

    def collectInfo(self):
        print("Creating Snapshot - Switch")
        self.getDeviceSwitchPorts()
        self.getDeviceSwitchRoutingInterfaceDhcp()
        self.getDeviceSwitchRoutingInterfaces()
        self.getDeviceSwitchRoutingStaticRoutes()
        self.getDeviceSwitchWarmSpare()
        return self.snapshot
    # defines all push calls

    def pushInfo(self):
        print("Pushing Snapshot - Switch")
        self.putDeviceSwitchPorts()
        self.putDeviceSwitchWarmSpare()
        self.delDeviceSwitchRoutingInterface()
        self.delDeviceSwitchRoutingInterfaceDhcp()
        self.delDeviceSwitchRoutingStaticRoute()
        self.postDeviceSwitchRoutingInterfaces()
        self.postDeviceSwitchRoutingInterfaceDhcp()
        self.postDeviceSwitchRoutingStaticRoutes()

# end of switch script
