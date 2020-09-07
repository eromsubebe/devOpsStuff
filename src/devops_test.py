import requests
import json

url = "https://api.macaddress.io/v1?output=json"
macId = input('Mac Address in Format "Example 44:38:39:ff:ef:57": ')
macId = macId.strip('')

payload = {}
headers = {
  'X-Authentication-Token': 'at_V5B4wI5ldyLYpV9NSM5NnAFkTO6Jz'
}
response = requests.request("GET", url + "&search={}".format(macId), headers=headers, data = payload)

r = response.json().get('vendorDetails')
if 'companyName' in r:
    print('Company name matching MAC address {} is: {}'.format(macId,r['companyName']))
else:
    print('No valid Company name matching MAC address {}'.format(macId))
print()
