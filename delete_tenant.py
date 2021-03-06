#!/usr/bin/env python

import json
import requests
import sys

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
post_response = requests.post("https://10.1.6.120/api/aaaLogin.json", data=json.dumps(name_pwd), verify=False)

#print post_response.text


# get token from login response structure
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

# create cookie array from token
cookies = {}
cookies['APIC-Cookie'] = auth_token


#BD
count = 1
#bd = {"totalCount":"1","imdata":[{"fvBD":{"attributes":{"arpFlood":"no","descr":"","dn":"uni/tn-A40_'''+str(tenant_name)+'''/BD-core_bd_2","epMoveDetectMode":"","limitIpLearnToSubnets":"no","llAddr":"::","mac":"00:22:BD:F8:19:FF","multiDstPktAct":"bd-flood","name":"core_bd_2","ownerKey":"","ownerTag":"","unicastRoute":"no","unkMacUcastAct":"proxy","unkMcastAct":"flood","vmac":"not-applicable"},"children":[{"fvRsBDToNdP":{"attributes":{"tnNdIfPolName":""}}},{"fvRsCtx":{"attributes":{"tnFvCtxName":"'''+str(tenant_name)+'''_vrf_prod"}}},{"fvRsIgmpsn":{"attributes":{"tnIgmpSnoopPolName":""}}},{"fvRsBdToEpRet":{"attributes":{"resolveAct":"resolve","tnFvEpRetPolName":""}}}]}}]}
while count <= int(sys.argv[1]):
    tenant_name = "n"+str(count)
    tenant = '''
    <?xml version="1.0" encoding="UTF-8"?>
    <imdata totalCount="1">
        <fvTenant name="A40_'''+str(tenant_name)+'''" status="deleted"/>
    </imdata>
    '''
    # read a sensor, incorporating token in request
    sensor_url = base_url + 'mo/uni.xml'
    get_response = requests.post(sensor_url, cookies=cookies,data=tenant, verify=False)

    # display sensor data structure
    count = count+1
    print "Delete Tenant: "+tenant_name+" "+str(get_response)
