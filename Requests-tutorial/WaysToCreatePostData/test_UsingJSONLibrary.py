import json

import requests
import pytest

class TestCreateStudentUsingJSONLib:

    @pytest.fixture(autouse=True)
    def setUp_and_tearDown(self):
        self.base_url="http://localhost:3000/students"
        self.student_data=\
                        {
                            'name': 'TestStudent',
                            'location': 'Test Location',
                            'phone no': '+8907654321',
                            'courses': ['Test', 'Course']
                        }
        self.headers = {'Content-Type':'application/json'}

        yield
        url = f"{self.base_url}/{self.student_id}"
        delete_res = requests.delete(url=url)
        assert delete_res.status_code == 200
        print(json.dumps(delete_res.json(),indent=4))

    def test_addStudentUsingJSONMoudule(self):
        res = requests.post(url=self.base_url,data=json.dumps(self.student_data),headers=self.headers)
        assert res.status_code == 201
        self.student_id = res.json()['id']
        print("Post URL: ", self.base_url)
        print(json.dumps(res.json(), indent=4))