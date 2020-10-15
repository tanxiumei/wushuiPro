import MySQLdb

import pytest
import xlrd

#连接数据库服务
conn = MySQLdb.connect(
    user='root',
    passwd='123456',
    host='localhost',
    port=3306,
    db='testing_db'
)

#读取Excel文件，获取里面的内容
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

#从表中查询出数据
def get_data():
    query_sql = 'select id,username,pwd from user_table'
    lst = []
    try:
        cursor = conn.cursor()  # 创建游标对象，发送sql语句
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


#向数据库中插入数据
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

#参数化数据
@pytest.mark.parametrize('id, name, pwd', get_data())
def tes1t1(id, name, pwd):
    print(id, name, pwd)

#执行程序
if __name__ == '__main__':
    pytest.main(['-sv', 'test_db.py'])
