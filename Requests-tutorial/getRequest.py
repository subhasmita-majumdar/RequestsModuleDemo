import json
from xml.etree.ElementTree import indent

import requests

def getAllStudents(url):
    response = requests.get(url)
    json_response = response.json()
    json_pretty = json.dumps(json_response,indent=5)
    assert response.status_code == 200
    print(json_pretty)

base_url="http://localhost:3000"
resource="/students"
url=base_url+resource
getAllStudents(url)