#!/usr/bin/env python

import json
import requests

base_url = 'https://10.1.6.120/api/'

# create credentials structure
name_pwd = {
  "aaaUser" : {
    "attributes" : {
      "name" : "admin",
      "pwd" : "C15co123!"
    }
  }
}
json_credentials = json.dumps(name_pwd)

# log in to API
login_url = base_url + 'aaaLogin.json'
print login_url
post_response = requests.post("https://10.1.6.120/api/aaaLogin.json", data=json.dumps(name_pwd), verify=False)

print post_response

"""
# get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token

# read a sensor, incorporating token in request
sensor_url = base_url + 'mo/topology/pod-1/node-101/sys/ch/bslot/board/sensor-3.json'
get_response = requests.get(sensor_url, cookies=cookies, verify=False)

# display sensor data structure
print get_response.json()
"""
