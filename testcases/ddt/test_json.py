import pytest
import json
def getData():
    with open("test.json") as f:
        list1 = []
        data = json.load(f)
        list1.extend(data["keys"])
        return list1
@pytest.mark.parametrize('name',getData())
def test01(name):
    print(name)
if __name__ == '__main__':
    pytest.main(['-sv','test_json.py'])