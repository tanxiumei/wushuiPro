import MySQLdb

import pytest
import xlrd

#�������ݿ����
conn = MySQLdb.connect(
    user='root',
    passwd='123456',
    host='localhost',
    port=3306,
    db='testing_db'
)

#��ȡExcel�ļ�����ȡ���������
def get_excel_Data():
    filename = 'db_data.xlsx'
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    list1 = []
    list2 = []
    for row in range(rows):
        for col in range(cols):
            cellData = sheet.cell_value(row, col)
            list1.append(cellData)
        list2.append(list1)
        list1 = []
    return list2

#�ӱ��в�ѯ������
def get_data():
    query_sql = 'select id,username,pwd from user_table'
    lst = []
    try:
        cursor = conn.cursor()  # �����α���󣬷���sql���
        cursor.execute(query_sql)
        r = cursor.fetchall()
        for x in r:
            u = (x[0], x[1], x[2])
            lst.append(u)
        return lst
    finally:
        # cursor.close()
        # conn.close()
        pass


#�����ݿ��в�������
def test2_insert_data():
    cursor = conn.cursor()
    list_data = get_excel_Data()
    print(11111)
    print(list_data)
    for data in list_data:
        # query_sql = f"insert into user_table values(9,'aa','123')"
        id = int(data[0])
        username = data[1]
        password = data[2]
        try:
            cursor.execute(f"insert into user_table values({id},'{username}','{password}')")
            r = cursor.fetchall()
            conn.commit()
        finally:
            pass
    cursor.close()
    conn.close()

#����������
@pytest.mark.parametrize('id, name, pwd', get_data())
def tes1t1(id, name, pwd):
    print(id, name, pwd)

#ִ�г���
if __name__ == '__main__':
    pytest.main(['-sv', 'test_db.py'])
