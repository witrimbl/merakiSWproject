import meraki
import json
import requests


class Wireless:
    def __init__(self, serial, networkID, apiKey, dictionary={}):
        self.device = "Wireless"
        self.serial = serial
        self.networkID = networkID
        self.dashboard = meraki.DashboardAPI(
            api_key='exampleKey', base_url='https://api.meraki.com/api/v1', print_console=False)  # input second api key for the api_key= section
        self.snapshot = dictionary
        self.apiKey = apiKey

    # GET
    def getDeviceBluetooth(self):
        try:
            response = self.dashboard.wireless.getDeviceWirelessBluetoothSettings(
                self.serial)
            self.snapshot['DeviceBluetooth'] = response
            # print(response)
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    def getDeviceRadio(self):
        try:
            response = self.dashboard.wireless.getDeviceWirelessRadioSettings(
                self.serial)
            #print(json.dumps(response, indent=2))
            self.snapshot['DeviceRadio'] = response
        except meraki.APIError as e:
            print("Meraki API error: ", {e})
            pass
        except Exception as e:
            print("some other error: ", {e})
            pass

    # PUT
    def putDeviceBluetooth(self):
        try:
            url = f"https://api.meraki.com/api/v1//devices/{self.serial}/wireless/bluetooth/settings"
            payload = json.dumps(self.snapshot['DeviceBluetooth'])
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

    def putDeviceRadio(self):
        try:
            url = f"https://api.meraki.com/api/v1//devices/{self.serial}/wireless/radio/settings"
            payload = json.dumps(self.snapshot['DeviceRadio'])
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

    # Collect and Push
    def collectInfo(self):
        print("Creating Snapshot - Wireless")
        self.getDeviceBluetooth()
        self.getDeviceRadio()
        return self.snapshot

    def pushInfo(self):
        print("Pushing Snapshot - Wireless")
        self.putDeviceBluetooth()
        self.putDeviceRadio()

# end of wireless script
