import json

import requests

base_url="http://localhost:3000"
path_param="/students"
query_param={'id':"1"}
url=base_url+path_param
response = requests.get(url=url,params=query_param)
assert response.status_code == 200
json_res = response.json()
json_pretty=json.dumps(json_res,indent=4)
print(type(json_res))
print(json_pretty)