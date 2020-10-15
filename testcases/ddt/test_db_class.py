import MySQLdb

import pytest
conn = MySQLdb.connect(
            user='root',
            passwd='123456',
            host='localhost',
            port=3306,
            db='testing_db'
        )
class Test_db(object):
    def setup_class(self):
        print("类前运行")
        self.conn = conn
        self.cursor = self.conn.cursor()  # 创建游标对象，发送sql语句

    def teardown_class(self):
        print("类后运行")
        self.cursor.close()
        self.conn.close()

    def get_data(self):
        query_sql = 'select id,username,pwd from user_table'
        lst = []
        try:
            #cursor = self.conn.cursor()  # 创建游标对象，发送sql语句
            self.cursor.execute(query_sql)
            r = self.cursor.fetchall()
            for x in r:
                u = (x[0], x[1], x[2])
                lst.append(u)
            return lst
        finally:
            # cursor.close()
            # conn.close()
            pass

    def te1st2_insert_data(self):
        cursor = self.conn.cursor()
        for x in range(10):
            # query_sql = f"insert into user_table values(9,'aa','123')"
            try:

                cursor.execute(f"insert into user_table values({x},'username{x + 1}','123')")
                r = cursor.fetchall()
                self.conn.commit()
            finally:
                pass

    @pytest.mark.parametrize('id, name, pwd', get_data())
    def test1(id, name, pwd):
        print(id, name, pwd)

if __name__ == '__main__':
    pytest.main(['-sv', 'test_db_class.py'])
