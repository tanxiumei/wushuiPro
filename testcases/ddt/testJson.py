import pytest
import json

def getData():
    with open('test.json') as f:
        data1 = json.load(f)
        lst = []
        lst.extend(data1['keys'])
    return lst
@pytest.mark.parametrize('name',getData())
def test01(name):
    print(name)

if __name__=='__main__':
    pytest.main(['-sv','testJson.py'])