import json
import requests

def updateExistingUser(url, bearer_token):
    headers={"Authorization":bearer_token}
    request_body=\
        {
            "name": "Aagney Singha",
            "gender": "male",
            "email": "Aagney.Singha@gleason.testm",
            "status": "inactive"
        }
    response = requests.put(url=url,headers=headers,json=request_body)
    json_res=response.json()
    json_pretty_res=json.dumps(json_res,indent=5)
    print(json_pretty_res)
    assert response.status_code == 200
    assert json_res["email"] == request_body["email"]

base_url="https://gorest.co.in"
resource="/public/v2/users/8080749"
url=base_url+resource
token_val="Bearer cd90ba7b6355af9986e75dd66f9af76a56a55fcd52f5579f3d56691c8d89d3c2"
updateExistingUser(url,token_val)