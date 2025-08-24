import json
import requests

def createNewUser(url,bearer_token):
    headers={"Authorization":bearer_token}
    data={
            "name": "Champaklal Gadha",
            "gender": "male",
            "email": "champaklal.gadha@vyapari.com",
            "status": "active"
        }
    response=requests.post(url=url,headers=headers,json=data)
    json_response=response.json()
    json_pretty_res=json.dumps(json_response,indent=5)
    assert response.status_code == 201
    assert json_response["name"] == data["name"]
    assert json_response["gender"] == data["gender"]
    assert json_response["email"] == data["email"]
    assert json_response["status"] == data["status"]
    print(json_pretty_res)


base_url="https://gorest.co.in"
resource="/public/v2/users"
url=base_url+resource
token_val="Bearer cd90ba7b6355af9986e75dd66f9af76a56a55fcd52f5579f3d56691c8d89d3c2"
createNewUser(url,token_val)
