#from testcases import testcase1,testcase02
#from util import util
#from testcases.basic.test_user_login import TestUserLogin
#from testcases.basic.test_admin_login import TestAdminLogin
#from testcases.basic.test_category import TestCategory
#from testcases.basic.test_article import TestArticle
#from lib.test_resport.HTMLTestRunner_PY3 import HTMLTestRunner
import pytest

from testcases.basic.naxinDispatch import NaxinDispatch
from testcases.basic.naxinLogin import TestAdminLogin
from testcases.basic.naxin_user_login import NaxinUserLogin
from testcases.basic.naxin_device_list import NaxinTestArticle
import csv
from faker import Faker
import datetime
from time import sleep
from xpinyin import Pinyin
def tes2t01():
    faker = Faker(locale='zh_CN')

    file = open('testData.csv', 'w',newline='')
    fwrite = csv.writer(file)
    """
    name = 'txm'
    start = datetime.date.today()
    for i in range(1,11):
        #print(i)
        num = str(i).zfill(5)
        tName = name+num
        tanname = faker.name()
        end = faker.date_between(start_date=start, end_date='+20d')
        phoneNum = faker.phone_number()
        ssnNum = faker.ssn(min_age=18,max_age=80)
        email = faker.free_email()
        fwrite.writerow([tName,tanname,start,end,phoneNum,ssnNum,email])

        #print(tName)
    
    """
    p = Pinyin()
    faker1 = Faker()
    for i in range(1, 2):
        # print(i)
        tanname = faker.name()
        phoneNum = faker.phone_number()
        #username = p.get_pinyin(faker.name(''))
        username = faker1.first_name()
        password = '111111'
        picFile = 'C:/Users/dell/Pictures/mingxing/44.png'
        fwrite.writerow([ tanname,phoneNum,username,password,picFile])

        # print(tName)
    file.close()



if __name__ == '__main__':

    #login = NaxinUserLogin()
    #login.test_user_login_ok()
    #addCase = NaxinDispatch(login)
    #addCase.testPatchChaxun()
    #addCase.testAddPatch()
    #addCase.testPatchChaxun()
    pytest.main(['-sv', './testcases/pytest'])







