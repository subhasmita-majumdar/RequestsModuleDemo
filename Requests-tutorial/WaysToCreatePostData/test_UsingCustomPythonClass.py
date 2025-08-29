import json

import requests
import pytest
from StudentClass import Students

class TestUsingPythonClass:
    @pytest.fixture(autouse=True)
    def setUp_and_tearDown(self):
        self.base_url = "http://localhost:3000/students"
        student = Students('Shilpi','Austria','+6213457890',['TS','JS'])
        self.student_data=student.to_dict()

        yield
        url = f"{self.base_url}/{self.student_id}"
        res = requests.delete(url=url)
        assert res.status_code == 200
        print("Deleted Record using: ",url)
        print(json.dumps(res.json(),indent=5))

    def test_addStudentUsingPythonClass(self):
        res = requests.post(url=self.base_url,json=self.student_data)
        assert res.status_code == 201
        self.student_id = res.json()['id']
        print("Post URL: ", self.base_url)
        print(json.dumps(res.json(), indent=4))