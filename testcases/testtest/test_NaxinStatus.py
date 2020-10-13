
from time import sleep

import self as self
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import pytest
import csv
import os
from xpinyin import Pinyin

from testcases.basic.naxinLogin import TestAdminLogin
#from testcases.basic.naxin_user_login import NaxinUserLogin
from testcases.basic.naxin_user_login import NaxinUserLogin
#from testcases.pytest.naxin_user_login import TestNaxinUserLogin
import random


def setData1():
    print('这是setdata函数')
    faker = Faker(locale='zh_CN')
    file = open('deviceData.csv', 'w', newline='')
    fwrite = csv.writer(file)
    p = Pinyin()
    faker1 = Faker()
    for i in range(1,2):
        deciveName = "设备名称"+str(faker.random_number(6))
        deciveNumber = faker.random_int()
        deciveXinghao = str(faker.random_int())+str(faker.random_digit_not_null())
        decivePinpai = "设备品牌"+str(faker.random_number(4))
        runTime =faker.random_int(4)
        firstTime=faker.past_date()#随机生成已经过去的日期
        lastTime =faker.future_date()#未来日期
        recentTime=faker.date_between(start_date='-30y', end_date=firstTime)
        purchaserName=faker.name()
        picFile = 'C:/Users/dell/Pictures/mingxing/fengji.jpg'
        fwrite.writerow([deciveName, deciveNumber, deciveXinghao,decivePinpai, runTime, firstTime,lastTime,recentTime,purchaserName,picFile])
    file.close()

#获取csv文件里的内容，返回一个包含list的list
def getData():
    setData1()
    print("这是getdata函数")
    csvFile = 'deviceData.csv'
    print(csvFile)
    with open(csvFile) as f:
        rows = csv.reader(f)
        myData = []
        temp = []
        for row in rows:
            temp.extend(row)
            myData.append(temp)
            temp = []
    print(myData)
    f.close()
    return myData


class TestNaxinStatus(object):
    #@pytest.mark.skip(reason="暂时不执行")
    def test_StatusList(self,userlogin):
        self.login = userlogin
        sleep(3)
        self.login.driver.find_element_by_id('/devicemanage').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div').click()
        windows = self.login.driver.window_handles
        self.login.driver.switch_to.window(windows[-1])
        #assert "设备详情" in self.login.driver.page_source
        assert "设备名称" in self.login.driver.page_source
        sleep(5)
        self.login.driver.back()

   # @pytest.mark.skip(reason="调试")
    @pytest.mark.parametrize('list2',getData())
    def test_AddUser(self,userlogin,list2):
        self.login = userlogin
        self.login.driver.refresh()
        #setDate()
        #deciveName, deciveNumber, deciveXinghao,decivePinpai, runTime, firstTime,lastTime,recentTime,purchaserName,picFile]
        list1 = list2
        print(list1)
        deciveName = list1[0]
        deciveNumber = list1[1]
        deciveXinghao = list1[2]
        decivePinpai = list1[3]
        runTime =list1[2]
        firstTime = list1[5]
        lastTime = list1[6]
        recentTime = list1[7]
        purchaserName = list1[8]
        picFile = list1[9]
        sleep(3)
        self.login.driver.find_element_by_id('/devicemanage').click()
        sleep(3)
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[5]').click()
        sleep(3)
        #定位设备名称
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(deciveName)
        #定位所属站点
        townNum = random.randint(1, 3)
        siteNum = random.randint(1, 2)
        deciveNum = random.randint(1, 4)
        # self.login.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li['+str(weixiuNum)+']').click()

        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input').click()
        sleep(1)#'+str(townNum)+'
        #self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[1]').click()
        #self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/ul/li[1]').click()
        self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/ul/li['+str(townNum)+']').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/ul/li['+str(siteNum)+']').click()

        #定位设备类型 /html/body/div[9]/div[1]/div[1]/ul/li[1]
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div/input').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li['+str(deciveNum)+']').click()

        #self.login.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        #/html/body/div[5]/div[1]/div[1]/ul/li[1]

        picFile = 'C:/Users/dell/Pictures/mingxing/'+str(deciveNum)+'.jpg'

        #定位设备编号
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[3]/div/div[1]/input').send_keys(deciveNumber)

        #定位设备型号
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[4]/div/div[1]/input').send_keys(deciveXinghao)


        #定位设备品牌
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[5]/div/div[1]/input').send_keys(decivePinpai)


        #定位运行时长
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[6]/div/div[1]/input').send_keys(runTime)


        #定位投入时间
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[7]/div/div/input').send_keys(firstTime)

        #定位质保期
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[8]/div/div/input').send_keys(lastTime)

        #定位最近维保时间
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[9]/div/div/input').send_keys(recentTime)

        #定位采购人

        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[10]/div/div[1]/input').send_keys(purchaserName)

        #定位运行状态
        statusNum = random.randint(1, 2)
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[11]/div/div/div/input').click()
        self.login.driver.find_element_by_xpath('/html/body/div[9]/div[1]/div[1]/ul/li['+str(statusNum)+']').click()


        #定位封面图片
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div')
        self.login.driver.find_element_by_name("file").send_keys(picFile)

        sleep(3)

        #定位确定按钮
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/button[2]').click()
        self.login.driver.refresh()



        #人员职位有4个，是下拉按钮显示的，所以设置一个随机生成数，可以随机选择职位
        weixiuNum = random.randint(1,4)
        print(weixiuNum)
        #self.login.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li['+str(weixiuNum)+']').click()
        sleep(3)

        """
        #提交成功之后，获取页面提示框信息
        loc = (By.CLASS_NAME,'el-message--success')
        WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        print("msg的值："+msg)
        print("保存成功！")
        assert msg == "保存成功！"
        assert username in self.login.driver.page_source
        """
if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinStatus.py'])






