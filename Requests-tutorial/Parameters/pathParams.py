import json

import requests

def createStudent(base_url):
    url = base_url+"/students"
    print("Post URL: ",url)
    student_data={
            "name": "Emma",
            "location": "Las Vegas",
            "phone": "+32123456",
            "courses": [
                "Acting",
                "Dancing"
            ]
        }
    response = requests.post(url=url,json=student_data)
    json_res=response.json()
    assert response.status_code == 201
    assert json_res["name"] == student_data["name"]
    assert json_res["location"] == student_data["location"]
    assert json_res["phone"] == student_data["phone"]
    assert json_res["courses"][0] == "Acting"
    assert json_res["courses"][1] == "Dancing"
    json_pretty=json.dumps(json_res,indent=5)
    print(json_pretty)
    s_id=json_res["id"]
    return s_id

def getStudentRecord(student_id,base_url):
    url = base_url+"/students/{}".format(student_id)
    print("Get URL: ",url)
    getRes = requests.get(url=url)
    assert getRes.status_code == 200
    json_getRes=getRes.json()
    json_getRes_pretty = json.dumps(json_getRes,indent=5)
    print(json_getRes_pretty)
    assert json_getRes["id"] == student_id

def updateStudentRecord(student_id,base_url):
    url = base_url + "/students/{}".format(student_id)
    print("Put URL: ", url)
    updated_student_data = {
        "name": "Emma Stone",
        "location": "Las Vegas",
        "phone": "+32123456",
        "courses": [
            "Acting",
            "Dancing"
        ]
    }
    putRes = requests.put(url=url,json=updated_student_data)
    assert putRes.status_code == 200
    json_putRes = putRes.json()
    json_putRes_pretty = json.dumps(json_putRes, indent=5)
    print(json_putRes_pretty)
    assert json_putRes["id"] == student_id
    assert json_putRes["name"] == updated_student_data["name"]

def deleteStudentRecord(student_id,base_url):
    url = base_url+"/students/{}".format(student_id)
    print("Delete URL: ",url)
    deleteRes = requests.delete(url=url)
    assert deleteRes.status_code == 200
    json_deleteRes=deleteRes.json()
    json_deleteRes_pretty = json.dumps(json_deleteRes,indent=5)
    print(json_deleteRes_pretty)
    assert json_deleteRes["id"] == student_id

base_url="http://localhost:3000"
student_id=createStudent(base_url)
getStudentRecord(student_id,base_url)
updateStudentRecord(student_id,base_url)
deleteStudentRecord(student_id,base_url)