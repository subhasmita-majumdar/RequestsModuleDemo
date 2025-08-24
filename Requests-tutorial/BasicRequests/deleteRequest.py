import requests

def deleteExistingUser(url,bearer_token):
    headers={"Authorization":bearer_token}
    response=requests.delete(url=url,headers=headers)
    assert response.status_code == 204

    get_response=requests.get(url=url,headers=headers)
    json_res=get_response.json()
    assert get_response.status_code == 404
    assert json_res["message"] == 'Resource not found'

base_url="https://gorest.co.in"
resource="/public/v2/users/8080772"
url=base_url+resource
token_val="Bearer cd90ba7b6355af9986e75dd66f9af76a56a55fcd52f5579f3d56691c8d89d3c2"
deleteExistingUser(url,token_val)










