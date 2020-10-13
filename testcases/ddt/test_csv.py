import pytest
import csv

def get_data():
    with open('test.csv') as f:
        list1 = csv.reader(f)
        my_data = []
        for row in list1:
            my_data.extend(row)
        return my_data
@pytest.mark.parametrize('name',get_data())
def test01(name):
   print(name)

if __name__ == '__main__':
    pytest.main(['-sv', 'test_csv.py'])

