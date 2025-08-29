import json

import pytest
import requests

class TestCreateStudentUsingDict:

    @pytest.fixture(autouse=True)
    def setUp_and_tearDown(self):
        self.base_url = "http://localhost:3000/students"
        self.student_data = {'name': 'TestStudent',
                        'location': 'Test Location',
                        'phone no': '+8907654321',
                        'courses': ['Test', 'Course']
                        }

        yield
        url = f"{self.base_url}/{self.student_id}"
        res = requests.delete(url=url)
        assert res.status_code == 200
        print(json.dumps(res.json(),indent=4))

    def test_addStudentDataUsingDict(self):
        res = requests.post(url=self.base_url,json=self.student_data)
        assert res.status_code == 201
        print("Post URL: ",self.base_url)
        print(json.dumps(res.json(),indent=4))
        self.student_id = res.json()['id']


