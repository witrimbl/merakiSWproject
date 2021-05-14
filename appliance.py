import meraki
import json
import requests


class Appliance:  # defining the appliance/MX class
    # list of variable to be passed in
    def __init__(self, serial, networkID, orgID, apiKey, dictionary={}):
        self.device = "Appliance"
        self.serial = serial
        self.networkID = networkID
        self.orgID = orgID
        self.dashboard = meraki.DashboardAPI(
            api_key='exampleKey', base_url='https://api.meraki.com/api/v1', print_console=False)  # input second api key for the api_key= section
        self.snapshot = dictionary
        self.apikey = apiKey

# GET
# please note that these get requests will follow the same structure
# connectivity monitoring
    def getNetworkApplianceConnectivityMonitoringDestinations(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceConnectivityMonitoringDestinations(
                self.networkID)  # completes get request
            # saves response of get request in snapshot file
            self.snapshot['NetworkApplianceConnectivityMonitoringDestinations'] = response
            # print(response)
        except meraki.APIError as e:  # error handling
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # content filtering

    def getNetworkApplianceContentFiltering(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceContentFiltering(
                self.networkID)
            self.snapshot['NetworkApplianceContentFiltering'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # firewalls

    def getNetworkApplianceFirewallCellularFirewallRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallCellularFirewallRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallCellularFirewallRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # note the put for this is per service so you will have to iderate through the array that is given in the response, put looks for network ID and service name
    def getNetworkApplianceFirewallFirewalledServices(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallFirewalledServices(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallFirewalledServices'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallInboundFirewallRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallInboundFirewallRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallInboundFirewallRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallL3FirewallRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallL3FirewallRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallL7FirewallRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallL7FirewallRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallL7FirewallRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallOneToManyNatRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallOneToManyNatRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallOneToManyNatRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallOneToOneNatRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallOneToOneNatRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallOneToOneNatRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceFirewallPortForwardingRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceFirewallPortForwardingRules(
                self.networkID)
            self.snapshot['NetworkApplianceFirewallPortForwardingRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # ports

    # going to have to iterate through this one
    def getNetworkAppliancePorts(self):
        try:
            response = self.dashboard.appliance.getNetworkAppliancePorts(
                self.networkID)
            self.snapshot['NetworkAppliancePorts'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
    # security

    def getNetworkApplianceSecurityIntrusion(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceSecurityIntrusion(
                self.networkID)
            self.snapshot['NetworkApplianceSecurityIntrusion'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # need to add the orgID line in create snapshot below network ID to main file
    def getOrganizationApplianceSecurityIntrusion(self):
        try:
            response = self.dashboard.appliance.getOrganizationApplianceSecurityIntrusion(
                self.orgID)
            self.snapshot['OrganizationApplianceSecurityIntrusion'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceSecurityMalware(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceSecurityMalware(
                self.networkID)
            self.snapshot['NetworkApplianceSecurityMalware'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # settings
    def getNetworkApplianceSettings(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceSettings(
                self.networkID)
            self.snapshot['NetworkApplianceSettings'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # single lan
    def getNetworkApplianceSingleLan(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceSingleLan(
                self.networkID)
            self.snapshot['NetworkApplianceSingleLan'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # static routes (going to have to iterate through this in the put) might be a bit tricky since the put input will be an array
    def getNetworkApplianceStaticRoutes(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceStaticRoutes(
                self.networkID)
            self.snapshot['NetworkApplianceStaticRoutes'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # traffic shaping
    def getNetworkApplianceTrafficShaping(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShaping(
                self.networkID)
            self.snapshot['NetworkApplianceTrafficShaping'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # going to have to iterate through the put
    def getNetworkApplianceTrafficShapingCustomPerformanceClasses(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClasses(
                self.networkID)
            self.snapshot['NetworkApplianceTrafficShapingCustomPerformanceClasses'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceTrafficShapingRules(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShapingRules(
                self.networkID)
            self.snapshot['NetworkApplianceTrafficShapingRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceTrafficShapingUplinkBandwidth(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShapingUplinkBandwidth(
                self.networkID)
            self.snapshot['NetworkApplianceTrafficShapingUplinkBandwidth'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceTrafficShapingUplinkSelection(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShapingUplinkSelection(
                self.networkID)
            self.snapshot['NetworkApplianceTrafficShapingUplinkSelection'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # vlans
    def getNetworkApplianceVlans(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceVlans(
                self.networkID)
            self.snapshot['NetworkApplianceVlans'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # vpn
    def getNetworkApplianceVpnBgp(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceVpnBgp(
                self.networkID)
            self.snapshot['NetworkApplianceVpnBgp'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getNetworkApplianceVpnSiteToSiteVpn(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceVpnSiteToSiteVpn(
                self.networkID)
            self.snapshot['NetworkApplianceVpnSiteToSiteVpn'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getOrganizationApplianceVpnThirdPartyVPNPeers(self):
        try:
            response = self.dashboard.appliance.getOrganizationApplianceVpnThirdPartyVPNPeers(
                self.orgID)
            self.snapshot['OrganizationApplianceVpnThirdPartyVPNPeers'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getOrganizationApplianceVpnVpnFirewallRules(self):
        try:
            response = self.dashboard.appliance.getOrganizationApplianceVpnVpnFirewallRules(
                self.orgID)
            self.snapshot['OrganizationApplianceVpnVpnFirewallRules'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # warm spare
    def getNetworkApplianceWarmSpare(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceWarmSpare(
                self.networkID)
            self.snapshot['NetworkApplianceWarmSpare'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def collectInfo(self):  # creates a function for calling the get requests
        print("Creating Snapshot - Appliance")
        self.getNetworkApplianceConnectivityMonitoringDestinations()
        self.getNetworkApplianceContentFiltering()
        self.getNetworkApplianceFirewallCellularFirewallRules()
        self.getNetworkApplianceFirewallFirewalledServices()
        self.getNetworkApplianceFirewallInboundFirewallRules()
        self.getNetworkApplianceFirewallL3FirewallRules()
        self.getNetworkApplianceFirewallL7FirewallRules()
        self.getNetworkApplianceFirewallOneToManyNatRules()
        self.getNetworkApplianceFirewallOneToOneNatRules()
        self.getNetworkApplianceFirewallPortForwardingRules()
        self.getNetworkAppliancePorts()
        self.getNetworkApplianceSecurityIntrusion()
        self.getOrganizationApplianceSecurityIntrusion()
        self.getNetworkApplianceSecurityMalware()
        self.getNetworkApplianceSettings()
        self.getNetworkApplianceSingleLan()
        self.getNetworkApplianceStaticRoutes()
        self.getNetworkApplianceTrafficShaping()
        self.getNetworkApplianceTrafficShapingCustomPerformanceClasses()
        self.getNetworkApplianceTrafficShapingRules()
        self.getNetworkApplianceTrafficShapingUplinkBandwidth()
        self.getNetworkApplianceTrafficShapingUplinkSelection()
        self.getNetworkApplianceVlans()
        self.getNetworkApplianceVpnBgp()
        self.getNetworkApplianceVpnSiteToSiteVpn()
        self.getOrganizationApplianceVpnThirdPartyVPNPeers()
        self.getOrganizationApplianceVpnVpnFirewallRules()
        self.getNetworkApplianceWarmSpare()
        return self.snapshot


# start of put requests, again these out requests have very similar structures

# monitoring destinations

    def putNetworkApplianceConnectivityMonitoringDestinations(self):
        try:
            # url for put request
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/connectivityMonitoringDestinations"
            payload = json.dumps(
                self.snapshot['NetworkApplianceConnectivityMonitoringDestinations'])  # setting the payload as the corresponding portion of the snapshot
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Cisco-Meraki-API-Key": "self.apikey"
            }  # setting the headers for the request
            response = requests.request(
                'PUT', url, headers=headers, data=payload)  # executing the request
        except meraki.APIError as e:  # error handling
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass
# content filtering

    def putNetworkApplianceContentFiltering(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/contentFiltering"
            payload = json.dumps(
                self.snapshot['NetworkApplianceContentFiltering'])
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
# firewall

    def putNetworkApplianceFirewallCellularFirewallRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/cellularFirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallCellularFirewallRules'])
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

    def putNetworkApplianceFirewallFirewalledServices(self):
        try:
            # saves corresponding snapshot portion as a variable in order to iterate through the elements in the snapshot
            services = self.snapshot['NetworkApplianceFirewallFirewalledServices']
            for s in services:
                # request url
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/firewalledServices/{s['service']}"
                # uses each array element in the snapshot as a payload for a put request
                payload = json.dumps(s)
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }  # headers for request
                response = requests.request(
                    'PUT', url, headers=headers, data=payload)  # executes the out request
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def putNetworkApplianceFirewallInboundFirewallRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/inboundFirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallInboundFirewallRules'])
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

    def putNetworkApplianceFirewallL3FirewallRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/l3FirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallL3FirewallRules'])
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

    def putNetworkApplianceFirewallL7FirewallRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/l7FirewallRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallL7FirewallRules'])
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

    def putNetworkApplianceFirewallOneToManyNatRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/oneToManyNatRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallOneToManyNatRules'])
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

    def putNetworkApplianceFirewallOneToOneNatRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/oneToOneNatRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallOneToOneNatRules'])
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

    def putNetworkApplianceFirewallPortForwardingRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/firewall/portForwardingRules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceFirewallPortForwardingRules'])
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

# ports

    def putNetworkAppliancePorts(self):
        try:
            ports = self.snapshot['NetworkAppliancePorts']
            for p in ports:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/ports/{p['number']}"
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

# security
    def putNetworkApplianceSecurityIntrusion(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/security/intrusion"
            payload = json.dumps(
                self.snapshot['NetworkApplianceSecurityIntrusion'])
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

    def putOrganizationApplianceSecurityIntrusion(self):
        try:
            url = f"https://api.meraki.com/api/v1/organizations/{self.orgID}/appliance/security/intrusion"
            payload = json.dumps(
                self.snapshot['OrganizationApplianceSecurityIntrusion'])
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

    def putNetworkApplianceSecurityMalware(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/security/malware"
            payload = json.dumps(
                self.snapshot['NetworkApplianceSecurityMalware'])
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

# single lan
    def putNetworkApplianceSingleLan(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/singleLan"
            payload = json.dumps(
                self.snapshot['NetworkApplianceSingleLan'])
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

# static routes
    def putNetworkApplianceStaticRoutes(self):
        # this is the final format used for pushing the snapshot where the elements would need to be deleted first the created with a post request
        try:
            response = self.dashboard.appliance.getNetworkApplianceStaticRoutes(
                self.networkID)  # get request to get the elements in the target network (static routes in this case)
            holder = response  # stores response in a holder variable
            # print(response)
        except meraki.APIError as e:  # error handling
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            Static = holder  # sets veriavle static to the value of the holder variable
            for s in Static:  # iterates through elements of the variable static
                # url for delete request
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/staticRoutes/{s['id']}"
                payload = None  # no payload since it is a delete request
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }  # headers for delete request
                response = requests.request(
                    'DELETE', url, headers=headers, data=payload)  # execute delete request
        except meraki.APIError as e:  # error handling
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

        try:
            # sets new variable to the value of the corresponding part of the snapshot
            new = self.snapshot['NetworkApplianceStaticRoutes']
            for n in new:  # iterates through the array elements in the snapshot
                # url for post request
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/staticRoutes"
                payload = json.dumps(n)  # sets payload as snapshot element
                headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "X-Cisco-Meraki-API-Key": "self.apikey"
                }  # headers for post request
                response = requests.request(
                    'POST', url, headers=headers, data=payload)  # execute post request
        except meraki.APIError as e:  # error handling
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

# traffic shaping
    def putNetworkApplianceTrafficShaping(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping"
            payload = json.dumps(
                self.snapshot['NetworkApplianceTrafficShaping'])
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

# performance classes

    def putNetworkApplianceTrafficShapingCustomPerformanceClasses(self):

        try:
            response = self.dashboard.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClasses(
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
            perf = holder
            for p in perf:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping/customPerformanceClasses/{p['customPerformanceClassId']}"
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
            new = self.snapshot['NetworkApplianceTrafficShapingCustomPerformanceClasses']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping/customPerformanceClasses"
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

    def putNetworkApplianceTrafficShapingRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping/rules"
            payload = json.dumps(
                self.snapshot['NetworkApplianceTrafficShapingRules'])
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

    def putNetworkApplianceTrafficShapingUplinkBandwidth(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping/uplinkBandwidth"
            payload = json.dumps(
                self.snapshot['NetworkApplianceTrafficShapingUplinkBandwidth'])
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

    def putNetworkApplianceTrafficShapingUplinkSelection(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/trafficShaping/uplinkSelection"
            payload = json.dumps(
                self.snapshot['NetworkApplianceTrafficShapingUplinkSelection'])
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


# vlans

    def putNetworkApplianceVlans(self):
        try:
            response = self.dashboard.appliance.getNetworkApplianceVlans(
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
            vlan = holder
            for v in vlan:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/vlans/{v['id']}"
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
            new = self.snapshot['NetworkApplianceVlans']
            for n in new:
                url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/vlans"
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

# VPN
    def putNetworkApplianceVpnBgp(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/vpn/bgp"
            payload = json.dumps(
                self.snapshot['NetworkApplianceVpnBgp'])
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

    def putNetworkApplianceVpnSiteToSiteVpn(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/vpn/siteToSiteVpn"
            payload = json.dumps(
                self.snapshot['NetworkApplianceVpnSiteToSiteVpn'])
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

    def putOrganizationApplianceVpnThirdPartyVPNPeers(self):
        try:
            url = f"https://api.meraki.com/api/v1/organizations/{self.orgID}/appliance/vpn/thirdPartyVPNPeers"
            payload = json.dumps(
                self.snapshot['OrganizationApplianceVpnThirdPartyVPNPeers'])
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

    def putOrganizationApplianceVpnVpnFirewallRules(self):
        try:
            url = f"https://api.meraki.com/api/v1/organizations/{self.orgID}/appliance/vpn/vpnFirewallRules"
            payload = json.dumps(
                self.snapshot['OrganizationApplianceVpnVpnFirewallRules'])
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

# warm spare
    def putNetworkApplianceWarmSpare(self):
        try:
            url = f"https://api.meraki.com/api/v1/networks/{self.networkID}/appliance/warmSpare"
            payload = json.dumps(
                self.snapshot['NetworkApplianceWarmSpare'])
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

# push config
    def pushInfo(self):  # creates a function for calling all put requests
        print("Pushing Snapshot - Appliance")
        self.putNetworkApplianceConnectivityMonitoringDestinations()
        self.putNetworkApplianceContentFiltering()
        self.putNetworkApplianceFirewallCellularFirewallRules()
        self.putNetworkApplianceFirewallFirewalledServices()
        self.putNetworkApplianceFirewallInboundFirewallRules()
        self.putNetworkApplianceFirewallL3FirewallRules()
        self.putNetworkApplianceFirewallL7FirewallRules()
        self.putNetworkApplianceFirewallOneToManyNatRules()
        self.putNetworkApplianceFirewallOneToOneNatRules()
        self.putNetworkApplianceFirewallPortForwardingRules()
        self.putNetworkAppliancePorts()
        self.putNetworkApplianceSecurityIntrusion()
        self.putOrganizationApplianceSecurityIntrusion()
        self.putNetworkApplianceSecurityMalware()
        self.putNetworkApplianceSingleLan()
        self.putNetworkApplianceStaticRoutes()
        self.putNetworkApplianceTrafficShaping()
        self.putNetworkApplianceTrafficShapingCustomPerformanceClasses()
        self.putNetworkApplianceTrafficShapingRules()
        self.putNetworkApplianceTrafficShapingUplinkBandwidth()
        self.putNetworkApplianceTrafficShapingUplinkSelection()
        self.putNetworkApplianceVlans()
        self.putNetworkApplianceVpnBgp()
        self.putNetworkApplianceVpnSiteToSiteVpn()
        self.putOrganizationApplianceVpnThirdPartyVPNPeers()
        self.putOrganizationApplianceVpnVpnFirewallRules()
        self.putNetworkApplianceWarmSpare()

# End of Appliance code
