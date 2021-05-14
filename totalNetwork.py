import meraki
import json
import requests


class TotalNetwork:
    def __init__(self, networkID, apiKey, dictionary={}):
        self.device = "TotalNetwork"
        self.networkID = networkID
        self.dashboard = meraki.DashboardAPI(
            api_key='exampleKey', base_url='https://api.meraki.com/api/v1', print_console=False)  # input second API key from dashboard into the variable below (meraki.DashboardAPI(api_key=xxxxxx))
        self.snapshot = dictionary
        self.apiKey = apiKey

    # GET - Network Switch settings

    def getNetworkSwitchRoutingMulticast(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchRoutingMulticast(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchRoutingMulticast'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchRoutingMulticastRendezvousPoints(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchRoutingMulticastRendezvousPoints(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchRoutingMulticastRendezvousPoints'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchRoutingOspf(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchRoutingOspf(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchRoutingOspf'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchAccessControlLists(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchAccessControlLists(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchAccessControlLists'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchAccessPolicies(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchAccessPolicies(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchAccessPolicies'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchAlternateManagementInterface(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchAlternateManagementInterface(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchAlternateManagementInterface'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchDhcpServerPolicy(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchDhcpServerPolicy(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchDhcpServerPolicy'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchDscpToCosMappings(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchDscpToCosMappings(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchDscpToCosMappings'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchLinkAggregations(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchLinkAggregations(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchLinkAggregations'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchMtu(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchMtu(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchMtu'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchPortSchedules(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchPortSchedules(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchPortSchedules'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchQosRules(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchQosRules(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchQosRules'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchQosRulesOrder(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchQosRulesOrder(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchQosRulesOrder'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchSettings(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchSettings(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchSettings'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStacks(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchStacks'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStackRoutingInterfaces(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            stackRoutingInterfacesDict = {}
            for s in stacks:
                response = self.dashboard.switch.getNetworkSwitchStackRoutingInterfaces(
                    self.networkID, s['id'])
                stackRoutingInterfacesDict[s['id']] = response
            self.snapshot['NetworkSwitchStackRoutingInterfaces'] = stackRoutingInterfacesDict
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStackRoutingInterfaceDhcp(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            stackRoutingInterfaceDhcpDict = {}
            for s in stacks:
                stackRouteInterfaces = self.dashboard.switch.getNetworkSwitchStackRoutingInterfaces(
                    self.networkID, s['id'])
                perStackDhcp = {}
                for i in stackRouteInterfaces:
                    response = self.dashboard.switch.getNetworkSwitchStackRoutingInterfaceDhcp(
                        self.networkID, s['id'], i['interfaceId'])
                    perStackDhcp[i['interfaceId']] = response
                stackRoutingInterfaceDhcpDict[s['id']] = perStackDhcp
            self.snapshot['NetworkSwitchStackRoutingInterfaceDhcp'] = stackRoutingInterfaceDhcpDict
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStackRoutingStaticRoutes(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            stackRoutingStaticRoutesDict = {}
            for s in stacks:
                response = self.dashboard.switch.getNetworkSwitchStackRoutingStaticRoutes(
                    self.networkID, s['id'])
                stackRoutingStaticRoutesDict[s['id']] = response
            self.snapshot['NetworkSwitchStackRoutingStaticRoutes'] = stackRoutingStaticRoutesDict
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStormControl(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchStormControl(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchStormControl'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSwitchStp(self):
        try:
            response = self.dashboard.switch.getNetworkSwitchStp(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkSwitchStp'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # GET - General Network
    def getNetwork(self):
        try:
            response = self.dashboard.networks.getNetwork(self.networkID)
            self.snapshot['Network'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkAlertsSettings(self):
        try:
            response = self.dashboard.networks.getNetworkAlertsSettings(
                self.networkID)
            self.snapshot['NetworkAlertsSettings'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # request has two parameters (networkID & clientId)
    def getNetworkClientPolicy(self):
        try:
            response = self.dashboard.networks.getNetworkClientPolicy(
                self.networkID)
            self.snapshot['NetworkClientPolicy'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # request has two parameters (networkID & clientId)
    def getNetworkClientSplashAuthorizationStatus(self):
        try:
            response = self.dashboard.networks.getNetworkClientSplashAuthorizationStatus(
                self.networkID)
            self.snapshot['NetworkClientSplashAuthorizationStatus'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkDevices(self):
        try:
            response = self.dashboard.networks.getNetworkDevices(
                self.networkID)
            self.snapshot['NetworkDevices'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkFirmwareUpgrades(self):
        try:
            response = self.dashboard.networks.getNetworkFirmwareUpgrades(
                self.networkID)
            self.snapshot['NetworkFirmwareUpgrades'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # There are two GET requests under floor plan?? Do I treat them differently?
    def getNetworkFloorPlans(self):
        try:
            response = self.dashboard.networks.getNetworkFloorPlans(
                self.networkID)
            self.snapshot['NetworkFloorPlans'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # There are two GET requests under floor plan?? Do I treat them differently?
    def getNetworkGroupPolicies(self):
        try:
            response = self.dashboard.networks.getNetworkGroupPolicies(
                self.networkID)
            self.snapshot['NetworkGroupPolicies'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkMerakiAuthUsers(self):
        try:
            response = self.dashboard.networks.getNetworkMerakiAuthUsers(
                self.networkID)
            self.snapshot['NetworkMerakiAuthUsers'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkMqttBrokers(self):
        try:
            response = self.dashboard.networks.getNetworkMqttBrokers(
                self.networkID)
            self.snapshot['NetworkMqttBrokers'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkNetflow(self):
        try:
            response = self.dashboard.networks.getNetworkNetflow(
                self.networkID)
            self.snapshot['NetworkNetflow'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkPiiRequests(self):
        try:
            response = self.dashboard.networks.getNetworkPiiRequests(
                self.networkID)
            self.snapshot['NetworkPiiRequests'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSettings(self):
        try:
            response = self.dashboard.networks.getNetworkSettings(
                self.networkID)
            self.snapshot['NetworkSettings'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSnmp(self):
        try:
            response = self.dashboard.networks.getNetworkSnmp(self.networkID)
            self.snapshot['NetworkSnmp'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkSyslogServers(self):
        try:
            response = self.dashboard.networks.getNetworkSyslogServers(
                self.networkID)
            self.snapshot['NetworkSyslogServers'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkTrafficAnalysis(self):
        try:
            response = self.dashboard.networks.getNetworkTrafficAnalysis(
                self.networkID)
            self.snapshot['NetworkTrafficAnalysis'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkWebhooksHttpServers(self):
        try:
            response = self.dashboard.networks.getNetworkWebhooksHttpServers(
                self.networkID)
            self.snapshot['NetworkWebhooksHttpServers'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkWebhooksWebhookTest(self):
        try:
            response = self.dashboard.networks.getNetworkWebhooksWebhookTest(
                self.networkID)
            self.snapshot['NetworkWebhooksWebhookTest'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    #GET - Wireless
    def getNetworkBluetooth(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessBluetoothSettings(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkBluetooth'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getAlternateInterface(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessAlternateManagementInterface(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['AlternateInterface'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getBilling(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessBilling(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['Billing'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkWirelessRFProfiles(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessRfProfiles(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkWirelessRFProfiles'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkWirelessSettings(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessSettings(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['NetworkWirelessSettings'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkWirelessSSIDS(self):
        try:
            response = self.dashboard.wireless.getNetworkWirelessSsids(
                self.networkID)
            #print(json.dumps(response, indent=2))
            self.snapshot['GeneralNetworkWirelessSSIDs'] = response
            self.snapshot['NetworkWirelessSSIDs'] = {}
            for i in response:
                ssid = i['number']
                self.snapshot['NetworkWirelessSSIDs'][str(ssid)] = {}
                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidDeviceTypeGroupPolicies(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['GroupPolicies'] = res
                except Exception as e:
                    print("some other error: ", {e})
                    pass

                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidFirewallL3FirewallRules(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['L3FirewallRules'] = res
                except Exception as e:
                    print("some other error: ", {e})
                    pass

                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidFirewallL7FirewallRules(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['L7FirewallRules'] = res
                except Exception as e:
                    print("some other error: ", {e})
                    pass

                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidIdentityPsks(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['IdentityPsks'] = res

                except Exception as e:
                    print("some other error: ", {e})
                    pass

                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidSplashSettings(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['SplashSettings'] = res
                except Exception as e:
                    print("some other error: ", {e})
                    pass

                try:
                    res = self.dashboard.wireless.getNetworkWirelessSsidTrafficShapingRules(
                        self.networkID, ssid)
                    self.snapshot['NetworkWirelessSSIDs'][str(
                        ssid)]['TrafficShapingRules'] = res
                except Exception as e:
                    print("some other error: ", {e})
                    pass

        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def collectInfo(self):  # creates a function for calling the get requests
        print("Creating Snapshot - Network Total")
        self.getNetwork()
        self.getNetworkAlertsSettings()
        self.getNetworkClientPolicy()
        self.getNetworkClientSplashAuthorizationStatus()
        self.getNetworkDevices()
        self.getNetworkFirmwareUpgrades()
        self.getNetworkFloorPlans()
        self.getNetworkGroupPolicies()
        self.getNetworkMerakiAuthUsers()
        self.getNetworkMqttBrokers()
        self.getNetworkNetflow()
        self.getNetworkPiiRequests()
        self.getNetworkSettings()
        self.getNetworkSnmp()
        self.getNetworkSyslogServers()
        self.getNetworkTrafficAnalysis()
        self.getNetworkWebhooksHttpServers()
        self.getNetworkWebhooksWebhookTest()
        self.getNetworkSwitchAccessControlLists()
        self.getNetworkSwitchAccessPolicies()
        self.getNetworkSwitchAlternateManagementInterface()
        self.getNetworkSwitchDhcpServerPolicy()
        self.getNetworkSwitchDscpToCosMappings()
        self.getNetworkSwitchLinkAggregations()
        self.getNetworkSwitchMtu()
        self.getNetworkSwitchPortSchedules()
        self.getNetworkSwitchQosRules()
        self.getNetworkSwitchQosRulesOrder()
        self.getNetworkSwitchRoutingMulticast()
        self.getNetworkSwitchRoutingMulticastRendezvousPoints()
        self.getNetworkSwitchRoutingOspf()
        self.getNetworkSwitchSettings()
        self.getNetworkSwitchStacks()
        self.getNetworkSwitchStackRoutingInterfaces()
        self.getNetworkSwitchStackRoutingInterfaceDhcp()
        self.getNetworkSwitchStackRoutingStaticRoutes()
        self.getNetworkSwitchStormControl()
        self.getNetworkSwitchStp()
        self.getNetworkBluetooth()
        self.getAlternateInterface()
        self.getBilling()
        self.getNetworkWirelessRFProfiles()
        self.getNetworkWirelessSettings()
        self.getNetworkWirelessSSIDS()
        return self.snapshot

     # PUT -  Network Switch settings

    def putNetworkSwitchRoutingMulticast(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/routing/multicast"
            payload = json.dumps(
                self.snapshot['NetworkSwitchRoutingMulticast'])
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

    def putNetworkSwitchRoutingOspf(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/routing/ospf"
            payload = json.dumps(self.snapshot['NetworkSwitchRoutingOspf'])
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

    def putNetworkSwitchAlternateManagementInterface(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/alternateManagementInterface"
            payload = json.dumps(
                self.snapshot['NetworkSwitchAlternateManagementInterface'])
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

    def putNetworkSwitchAccessControlLists(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/accessControlLists"
            payload = json.dumps(
                self.snapshot['NetworkSwitchAccessControlLists'])
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

    def putNetworkSwitchDhcpServerPolicy(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/dhcpServerPolicy"
            payload = json.dumps(
                self.snapshot['NetworkSwitchDhcpServerPolicy'])
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

    def putNetworkSwitchDscpToCosMappings(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/dscpToCosMappings"
            payload = json.dumps(
                self.snapshot['NetworkSwitchDscpToCosMappings'])
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

    def putNetworkSwitchMtu(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/mtu"
            payload = json.dumps(self.snapshot['NetworkSwitchMtu'])
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

    def putNetworkSwitchQosRulesOrder(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/qosRules/order"
            payload = json.dumps(self.snapshot['NetworkSwitchQosRulesOrder'])
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

    def putNetworkSwitchSettings(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/settings"
            payload = json.dumps(self.snapshot['NetworkSwitchSettings'])
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

    def putNetworkSwitchStormControl(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stormControl"
            payload = json.dumps(self.snapshot['NetworkSwitchStormControl'])
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

    def putNetworkSwitchStp(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stp"
            payload = json.dumps(self.snapshot['NetworkSwitchStp'])
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

    def putNetworkSwitchStackRoutingInterfaceDhcp(self):
        try:
            ss = self.snapshot['NetworkSwitchStackRoutingInterfaceDhcp']
            for s in ss:
                for i in s:
                    url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s}/routing/interfaces/{i}/dhcp"
                    payload = json.dumps([s[i]])
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

    def delNetworkSwitchRoutingMulticastRendezvousPoints(self):
        try:
            points = self.dashboard.switch.getNetworkSwitchRoutingMulticastRendezvousPoints(
                self.networkID)
            for p in points:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/routing/multicast/rendezvousPoints/{p['rendezvousPointId']}"
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

    def delNetworkSwitchAccessPolicies(self):
        try:
            policies = self.dashboard.switch.getNetworkSwitchAccessPolicies(
                self.networkID)
            for p in policies:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/accessPolicies/{p['accessPolicyNumber']}"
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

    def delNetworkSwitchLinkAggregations(self):
        try:
            aggregations = self.dashboard.switch.getNetworkSwitchLinkAggregations(
                self.networkID)
            for a in aggregations:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/linkAggregations/{a['linkAggregationId']}"
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

    def delNetworkSwitchPortSchedules(self):
        try:
            schedules = self.dashboard.switch.getNetworkSwitchPortSchedules(
                self.networkID)
            for s in schedules:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/portSchedules/{s['portScheduleId']}"
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

    def delNetworkSwitchQosRules(self):
        try:
            rules = self.dashboard.switch.getNetworkSwitchQosRules(
                self.networkID)
            for r in rules:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/qosRules/{r['qosRuleId']}"
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

    def delNetworkSwitchStacks(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            for s in stacks:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s['switchStackId']}"
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

    def delNetworkSwitchStackRoutingInterfaces(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            for s in stacks:
                stackRouteInterfaces = self.dashboard.switch.getNetworkSwitchStackRoutingInterfaces(
                    self.networkID, s['id'])
                for i in stackRouteInterfaces:
                    url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s['switchStackId']}/interface/{i['interfaceId']}"
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

    def delNetworkSwitchStackRoutingStaticRoutes(self):
        try:
            stacks = self.dashboard.switch.getNetworkSwitchStacks(
                self.networkID)
            for s in stacks:
                stackStaticRoutes = self.dashboard.switch.getNetworkSwitchStackRoutingStaticRoutes(
                    self.networkID, s['id'])
                for r in stackStaticRoutes:
                    url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s['switchStackId']}/routing/staticRoutes/{r['staticRouteId']}"
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

    def postNetworkSwitchRoutingMulticastRendezvousPoints(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/routing/multicast/rendezvousPoints/"
            payload = self.snapshot['NetworkSwitchRoutingMulticastRendezvousPoints']
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

    def postNetworkSwitchAccessPolicy(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/accessPolicies"
            payload = self.snapshot['NetworkSwitchAccessPolicies']
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

    def postNetworkSwitchLinkAggregation(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/linkAggregation"
            payload = self.snapshot['NetworkSwitchLinkAggregations']
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

    def postNetworkSwitchPortSchedules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/portSchedules"
            payload = self.snapshot['NetworkSwitchPortSchedules']
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

    def postNetworkSwitchQosRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/qosRules"
            payload = self.snapshot['NetworkSwitchQosRules']
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

    def postNetworkSwitchStacks(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks"
            payload = self.snapshot['NetworkSwitchStacks']
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

    def postNetworkSwitchStackRoutingInterfaces(self):
        try:
            ss = self.snapshot['NetworkSwitchStackRoutingInterfaces']
            for s in ss:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s}/routing/interfaces"
                payload = self.snapshot[ss[s]]
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

    def postNetworkSwitchStackRoutingStaticRoutes(self):
        try:
            ss = self.snapshot['NetworkSwitchStackRoutingStaticRoutes']
            for s in ss:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/switch/stacks/{s}/routing/staticRoutes"
                payload = self.snapshot[ss[s]]
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

    def putNetwork(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}"
            payload = json.dumps(
                self.snapshot['Network'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # Update the alert configuration for this network

    def putNetworkAlertsSettings(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/alerts/settings"
            payload = json.dumps(
                self.snapshot['NetworkAlertsSettings'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # Update the policy assigned to a client on the network
    def putNetworkClientPolicy(self):
        try:
            # includes ClientId
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/clients/{clientId}/policy"
            payload = json.dumps(
                self.snapshot['NetworkClientPolicy'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkClientSplashAuthorizationStatus(self):
        try:
            # includes ClientId
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/clients/{clientId}/splashAuthorizationStatus"
            payload = json.dumps(
                self.snapshot['NetworkClientSplashAuthorizationStatus'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # Claim network device

    def putNetworkDevices(self):
        try:
            new = self.snapshot['NetworkDevices']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/devices/claim"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkFirmwareUpgrades(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/firmwareUpgrades"
            payload = json.dumps(
                self.snapshot['NetworkFirmwareUpgrades'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkFloorPlans(self):
        try:
            response = self.dashboard.networks.getNetworkFloorPlans(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            floors = holder
            for f in floors:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/floorPlans/{f['floorPlanId']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkFloorPlans']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/floorPlans"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkGroupPolicy(self):
        try:
            response = self.dashboard.networks.getNetworkGroupPolicies(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            policy = holder
            for p in policy:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/groupPolicies/{p['groupPolicyId']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkGroupPolicies']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/groupPolicies"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkMerakiAuthUser(self):
        try:
            response = self.dashboard.networks.getNetworkMerakiAuthUsers(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            user = holder
            for u in user:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/merakiAuthUsers/{u['id']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkMerakiAuthUsers']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/merakiAuthUsers"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkMqttBroker(self):
        try:
            response = self.dashboard.networks.getNetworkMqttBrokers(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            broker = holder
            for b in broker:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/mqttBrokers/{b['id']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkMqttBrokers']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/mqttBrokers"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkNetflow(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/netflow"
            payload = json.dumps(
                self.snapshot['NetworkNetflow'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkPiiRequest(self):
        try:
            response = self.dashboard.networks.getNetworkPiiRequests(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            pii = holder
            for p in pii:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/pii/requests/{p['requestId']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkPiiRequests']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/pii/requests"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkSettings(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/settings"
            payload = json.dumps(
                self.snapshot['NetworkSettings'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkSnmp(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/snmp"
            payload = json.dumps(
                self.snapshot['NetworkSnmp'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkSyslogServers(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/syslogServers"
            payload = json.dumps(
                self.snapshot['NetworkSyslogServers'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkTrafficAnalysis(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/trafficAnalysis"
            payload = json.dumps(
                self.snapshot['NetworkTrafficAnalysis'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkWebhooksHttpServer(self):
        try:
            response = self.dashboard.networks.getNetworkWebhooksHttpServers(
                self.networkID)
            holder = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            webhook = holder
            for w in webhook:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/webhooks/httpServers/{w['id']}"
                payload = None
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            new = self.snapshot['NetworkWebhooksHttpServers']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/webhooks/httpServers"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkWebhooksWebhookTest(self):
        try:
            new = self.snapshot['NetworkWebhooksWebhookTest']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/webhooks/webhookTests"
                payload = json.dumps(n)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'POST', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    #POST - Wireless
    def putBilling(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/billing"
            payload = json.dumps(self.snapshot['Billing'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkWirelessRFProfiles(self):
        try:
            profiles = self.snapshot['NetworkWirelessRFProfiles']
            for p in profiles:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/rfProfiles/{p['id']}"
                payload = json.dumps(p)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkWirelessSettings(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/settings"
            payload = json.dumps(self.snapshot['NetworkWirelessSettings'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkBluetooth(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/bluetooth/settings"
            payload = json.dumps(self.snapshot['NetworkBluetooth'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putAlternateInterface(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/alternateManagementInterface"
            payload = json.dumps(self.snapshot['AlternateInterface'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkWirelessSSIDs(self):
        try:
            SSIDs = self.snapshot['GeneralNetworkWirelessSSIDs']
            for s in SSIDs:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/rfProfiles/{s['number']}"
                payload = json.dumps(s)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'PUT', url, headers=headers, data=payload)
                number = str(s['number'])
                self.putDeviceTypeGroupPolicies(number)
                self.putL3FirewallRules(number)
                self.putL7FirewallRules(number)
                self.putIdentityPsks(number)
                self.putSplashSettings(number)
                self.putTrafficShapingRules(number)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putDeviceTypeGroupPolicies(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/deviceTypeGroupPolicies"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['GroupPolicies'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putL3FirewallRules(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/firewall/l3FirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['L3FirewallRules'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putL7FirewallRules(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/firewall/l7FirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['L7FirewallRules'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putIdentityPsks(self, number):
        try:
            Psks = self.snapshot['NetworkWirelessSSIDs'][number]['IdentityPsks']
            for ip in Psks:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/identityPsks/{ip['identityPskId']}"
                payload = json.dumps(ip)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }
                response = requests.request(
                    'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putSplashSettings(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/splash/settings"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['SplashSettings'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putTrafficShapingRules(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/trafficShaping/rules"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['TrafficShapingRules'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putVPN(self, number):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/wireless/ssids/{number}/vpn"
            payload = json.dumps(
                self.snapshot['NetworkWirelessSSIDs'][number]['VPN'])
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }
            response = requests.request(
                'PUT', url, headers=headers, data=payload)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def pushInfo(self):  # creates a function for calling all put requests
        print("Pushing Snapshot - Total Network")
        self.putNetwork()
        self.putNetworkAlertsSettings()
        self.putNetworkClientPolicy()
        self.putNetworkClientSplashAuthorizationStatus()
        self.putNetworkDevices()
        self.putNetworkFirmwareUpgrades()
        self.putNetworkFloorPlans()
        self.putNetworkGroupPolicy()
        self.putNetworkMerakiAuthUser()
        self.putNetworkMqttBroker()
        self.putNetworkNetflow()
        self.putNetworkPiiRequest()
        self.putNetworkSettings()
        self.putNetworkSnmp()
        self.putNetworkSyslogServers()
        self.putNetworkTrafficAnalysis()
        self.putNetworkWebhooksHttpServer()
        self.putNetworkWebhooksWebhookTest()
        self.putNetworkSwitchAccessControlLists()
        self.putNetworkSwitchAlternateManagementInterface()
        self.putNetworkSwitchDhcpServerPolicy()
        self.putNetworkSwitchDscpToCosMappings()
        self.putNetworkSwitchMtu()
        self.putNetworkSwitchQosRulesOrder()
        self.putNetworkSwitchRoutingMulticast()
        self.putNetworkSwitchRoutingOspf()
        self.putNetworkSwitchSettings()
        self.putNetworkSwitchStackRoutingInterfaceDhcp()
        self.putNetworkSwitchStormControl()
        self.putNetworkSwitchStp()
        self.delNetworkSwitchAccessPolicies()
        self.delNetworkSwitchLinkAggregations()
        self.delNetworkSwitchPortSchedules()
        self.delNetworkSwitchQosRules()
        self.delNetworkSwitchRoutingMulticastRendezvousPoints()
        self.delNetworkSwitchStackRoutingInterfaces()
        self.delNetworkSwitchStackRoutingStaticRoutes()
        self.delNetworkSwitchStacks()
        self.postNetworkSwitchAccessPolicy()
        self.postNetworkSwitchLinkAggregation()
        self.postNetworkSwitchPortSchedules()
        self.postNetworkSwitchQosRules()
        self.postNetworkSwitchRoutingMulticastRendezvousPoints()
        self.postNetworkSwitchStacks()
        self.postNetworkSwitchStackRoutingInterfaces()
        self.postNetworkSwitchStackRoutingStaticRoutes()
        self.putNetworkBluetooth()
        self.putAlternateInterface()
        self.putBilling()
        self.putNetworkWirelessRFProfiles()
        self.putNetworkWirelessSettings()
        self.putNetworkWirelessSSIDs()

#end of total network script