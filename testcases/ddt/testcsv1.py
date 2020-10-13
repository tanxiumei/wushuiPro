import pytest
import csv

def testData():
    with open('test.csv') as f:
        lst = csv.reader(f)
        temp = []
        for row in lst:
            temp.extend(row)
    return temp
@pytest.mark.parametrize('name',testData())
def test01(name):
    print(name)

if __name__ == '__main__':
    pytest.main(['-sv','testcsv1.py'])