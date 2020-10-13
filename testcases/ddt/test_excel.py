import pytest
import xlrd

def getData():
    filename = 'data.xlsx'
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    list1 = []
    for row in range(rows):
        for col in range(cols):
            cellData = sheet.cell_value(row,col)
            list1.append(cellData)
    print(list1)
    return list1
@pytest.mark.parametrize('name',getData())
def test01(name):
    print(name)
if __name__ == '__main__':
    pytest.main(['-sv','test_execl.py'])