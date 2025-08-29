import json

import requests
import pytest
from StudentDataClass import StudentsData

class TestUsingPythonDataClass:
    @pytest.fixture(autouse=True)
    def setUp_and_tearDown(self):
        self.base_url = "http://localhost:3000/students"
        student = StudentsData('Anu','England','+7890123456',['C','C++'])
        self.student_data=student.__dict__

        yield
        url = f"{self.base_url}/{self.student_id}"
        res = requests.delete(url=url)
        assert res.status_code == 200
        print("Deleted Record using: ",url)
        print(json.dumps(res.json(),indent=5))

    def test_addStudentUsingPythonDataClass(self):
        res = requests.post(url=self.base_url,json=self.student_data)
        assert res.status_code == 201
        self.student_id = res.json()['id']
        print("Post URL: ", self.base_url)
        print(json.dumps(res.json(), indent=4))