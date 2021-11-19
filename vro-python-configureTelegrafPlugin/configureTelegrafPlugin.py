import requests
import json
import urllib3

def configureTelegrafPlugin(context, inputs):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    if "verify" not in inputs.keys():
        inputs["verify"] = True
    print(inputs["verify"])
    headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'vRealizeOpsToken '+ inputs["token"]}
    r = requests.request('POST','https://'+inputs["vropsHost"]+'/suite-api/api/applications/agents/'+inputs["resId"]+'/services', data=inputs["pluginConfig"], headers=headers, verify=inputs["verify"])
    print(r.status_code)
    print(r.url)
    res = {'code':r.status_code, 'text':json.loads(r.text)}
    return(res)