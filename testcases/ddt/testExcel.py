import pytest
import xlrd
def getData():
    filename = 'data.xlsx'
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    lst = []
    for row in range(rows):
        for col in range(cols):
            cellData = sheet.cell_value(row,col)
            print(cellData)
            lst.append(cellData)
    return lst

@pytest.mark.parametrize('name',getData())
def test01(name):
    print(name)
if __name__ == '__main__':
    pytest.main(['-sv','testExcel.py'])