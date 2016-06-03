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
      <fvTenant descr="" dn="uni/tn-A40_'''+str(tenant_name)+'''" name="A40_'''+str(tenant_name)+'''" ownerKey="" ownerTag="">
        <drawCont>
          <drawInst info="{'{fvAp/epg}-{'''+str(tenant_name)+'''_epg_sap}':{'x':65,'y':360.5},'{fvAp/epg}-{'''+str(tenant_name)+'''_epg_test}':{'x':185,'y':360.5},'{fvAp/epg}-{'''+str(tenant_name)+'''_epg_fw}':{'x':305,'y':360.5},'{fvAp/contract}-{test}':{'x':180,'y':60.5},'{fvAp/contract}-{permit-any}':{'x':152,'y':10}}" oDn="uni/tn-A40_'''+str(tenant_name)+'''/ap-'''+str(tenant_name)+'''_app_profile"/>
        </drawCont>
        <fvBD arpFlood="yes" descr="" epMoveDetectMode="" limitIpLearnToSubnets="no" llAddr="::" mac="00:22:BD:F8:19:FF" multiDstPktAct="bd-flood" name="'''+str(tenant_name)+'''_bd_sap" ownerKey="" ownerTag="" unicastRoute="yes" unkMacUcastAct="flood" unkMcastAct="flood" vmac="not-applicable">
          <fvRsBDToNdP tnNdIfPolName=""/>
          <fvRsCtx tnFvCtxName="'''+str(tenant_name)+'''_vrf_prod"/>
          <fvRsIgmpsn tnIgmpSnoopPolName=""/>
          <fvSubnet ctrl="" descr="" ip="10.4.0.1/24" name="" preferred="no" scope="public" virtual="no"/>
          <fvRsBdToEpRet resolveAct="resolve" tnFvEpRetPolName=""/>
        </fvBD>
        <fvBD arpFlood="no" descr="" epMoveDetectMode="" limitIpLearnToSubnets="no" llAddr="::" mac="00:22:BD:F8:19:FF" multiDstPktAct="bd-flood" name="'''+str(tenant_name)+'''_bd_fw" ownerKey="" ownerTag="" unicastRoute="yes" unkMacUcastAct="proxy" unkMcastAct="flood" vmac="not-applicable">
          <fvRsBDToNdP tnNdIfPolName=""/>
          <fvRsCtx tnFvCtxName="'''+str(tenant_name)+'''_vrf_prod"/>
          <fvRsIgmpsn tnIgmpSnoopPolName=""/>
          <fvRsBdToEpRet resolveAct="resolve" tnFvEpRetPolName=""/>
        </fvBD>
        <fvBD arpFlood="yes" descr="" epMoveDetectMode="" limitIpLearnToSubnets="no" llAddr="::" mac="00:22:BD:F8:19:FF" multiDstPktAct="bd-flood" name="'''+str(tenant_name)+'''_bd_srv" ownerKey="" ownerTag="" unicastRoute="yes" unkMacUcastAct="proxy" unkMcastAct="opt-flood" vmac="not-applicable">
          <fvRsBDToNdP tnNdIfPolName=""/>
          <fvRsCtx tnFvCtxName="'''+str(tenant_name)+'''_vrf_prod"/>
          <fvRsIgmpsn tnIgmpSnoopPolName=""/>
          <fvSubnet ctrl="" descr="" ip="10.4.1.1/24" name="" preferred="no" scope="public" virtual="no"/>
          <fvRsBdToEpRet resolveAct="resolve" tnFvEpRetPolName=""/>
        </fvBD>
        <fvCtx descr="" knwMcastAct="permit" name="'''+str(tenant_name)+'''_vrf_prod" ownerKey="" ownerTag="" pcEnfDir="ingress" pcEnfPref="enforced">
          <fvRsBgpCtxPol tnBgpCtxPolName=""/>
          <fvRsCtxToExtRouteTagPol tnL3extRouteTagPolName=""/>
          <fvRsOspfCtxPol tnOspfCtxPolName=""/>
          <vzAny descr="" matchT="AtleastOne" name=""/>
          <fvRsCtxToEpRet tnFvEpRetPolName=""/>
        </fvCtx>
        <fvAp descr="" name="'''+str(tenant_name)+'''_app_profile" ownerKey="" ownerTag="" prio="unspecified">
          <fvAEPg descr="" isAttrBasedEPg="no" matchT="AtleastOne" name="'''+str(tenant_name)+'''_epg_fw" pcEnfPref="unenforced" prio="unspecified">
            <fvRsBd tnFvBDName="'''+str(tenant_name)+'''_bd_fw"/>
            <fvRsCustQosPol tnQosCustomPolName=""/>
            <fvRsProv matchT="AtleastOne" prio="unspecified" tnVzBrCPName="'''+str(tenant_name)+'''_contract_to_fw"/>
            <fvRsProv matchT="AtleastOne" prio="unspecified" tnVzBrCPName="test"/>
          </fvAEPg>
          <fvAEPg descr="" isAttrBasedEPg="no" matchT="AtleastOne" name="'''+str(tenant_name)+'''_epg_sap" pcEnfPref="unenforced" prio="unspecified">
            <fvRsCons prio="unspecified" tnVzBrCPName="'''+str(tenant_name)+'''_contract_srv_to_sap"/>
            <fvRsCons prio="unspecified" tnVzBrCPName="'''+str(tenant_name)+'''_contract_to_fw"/>
            <fvRsPathAtt descr="" encap="vlan-400" instrImedcy="immediate" mode="regular" primaryEncap="unknown" tDn="topology/pod-1/paths-102/pathep-[eth1/48]"/>
            <fvRsBd tnFvBDName="'''+str(tenant_name)+'''_bd_sap"/><fvRsCustQosPol tnQosCustomPolName=""/>
            <fvRsProv matchT="AtleastOne" prio="unspecified" tnVzBrCPName="permit-any"/>
            <fvRsProv matchT="AtleastOne" prio="unspecified" tnVzBrCPName="test"/>
          </fvAEPg>
          <fvAEPg descr="" isAttrBasedEPg="no" matchT="AtleastOne" name="'''+str(tenant_name)+'''_epg_test" pcEnfPref="unenforced" prio="unspecified">
            <fvRsCons prio="unspecified" tnVzBrCPName="permit-any"/>
            <fvRsPathAtt descr="" encap="vlan-401" instrImedcy="immediate" mode="regular" primaryEncap="unknown" tDn="topology/pod-1/paths-102/pathep-[eth1/48]"/>
            <fvRsBd tnFvBDName="'''+str(tenant_name)+'''_bd_srv"/>
            <fvRsCustQosPol tnQosCustomPolName=""/>
          </fvAEPg>
        </fvAp>
        <fvRsTenantMonPol tnMonEPGPolName=""/>
        <vzFilter descr="" name="'''+str(tenant_name)+'''_contract_sto_to_esx_Filter" ownerKey="" ownerTag=""/>
      </fvTenant>
    </imdata>
    '''
    # read a sensor, incorporating token in request
    sensor_url = base_url + 'mo.xml'
    get_response = requests.post(sensor_url, cookies=cookies,data=tenant, verify=False)

    # display sensor data structure
    count = count+1
    print "Create Tenant: "+tenant_name+" "+str(get_response)
