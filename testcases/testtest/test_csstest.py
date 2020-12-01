
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

#获取csv文件里的内容，返回一个包含list的list
from wushuiPro.util.ctrExcelFile import setDate, getData

class TestNaxinSettings(object):
    #def setup_class(self,userlogin):
     #   self.login = userlogin
    @pytest.mark.skip(reason="调试")
    def test_DelUser(self,userlogin):
        self.login = userlogin
        print('11111test')
        sleep(2)
        #self.login.driver.find_element_by_xpath('//*[@id="/setmanage"]').click()
        self.login.driver.find_element_by_id('/setmanage').click()
        sleep(1)
       # self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/div/button[2]').click()

        #el1 = self.login.driver.find_elements_by_css_selector('.app-operation .el-button.btn-del.el-button--default.el-button--mini').click()
        el1 = self.login.driver.find_elements_by_css_selector(
            '.app-operation .el-button.btn-del.el-button--default.el-button--mini')
        el2 = el1[1].click()
        sleep(2)

        self.login.driver.find_element_by_css_selector('.el-message-box__btns .el-button--primary').click()
        assert 1==1
        sleep(3)

    #@pytest.mark.skip(reason="调试")
    @pytest.mark.parametrize('list2',getData('testData.csv'))
    def test_AddUser(self,userlogin,list2):
        self.login = userlogin
        self.login.driver.refresh()
        list1 = list2
        print(list1)
        name = list1[0]
        number = list1[1]
        username = list1[2]
        password = list1[3]
        picFile = list1[4]
        sleep(3)
        self.login.driver.find_element_by_id('/setmanage').click()
        sleep(3)
        self.login.driver.find_element_by_css_selector('.el-serach.noborder').click()
        sleep(3)
        #定位人员姓名
        # self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/d'
        #                                   'iv[1]/input').send_keys(name)

        #self.login.driver.find_element_by_css_selector("#app form div label+div input:nth-child(1)").send_keys(name)
        self.login.driver.find_element_by_css_selector("#app div.el-dialog__body>form>div:nth-child(1) label+div input").send_keys(name)
        #定位人员职位
        sleep(2)
        self.login.driver.find_element_by_css_selector("#app div.el-dialog__body>form>div:nth-child(2) label+div input").click()
        sleep(2)
        #人员职位有4个，是下拉按钮显示的，所以设置一个随机生成数，可以随机选择职位
        weixiuNum = random.randint(1,4)
        print(weixiuNum)
        #self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li['+str(weixiuNum)+']').click()

        self.login.driver.find_element_by_css_selector('.v-modal+div li:nth-child(2)').click()
        sleep(3)
        #定位手机号码
        self.login.driver.find_element_by_css_selector('#app div.el-dialog__body>form>div:nth-child(3) label+div input').send_keys(number)
        #定位用户名
        self.login.driver.find_element_by_css_selector('#app div.el-dialog__body>form>div:nth-child(4) label+div input').send_keys(username)
        #定位密码
        self.login.driver.find_element_by_css_selector('#app div.el-dialog__body>form>div:nth-child(5) label+div input').send_keys(password)
        #上传头像
        #self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[6]/div/div/div')
        self.login.driver.find_element_by_name("file").send_keys(picFile)
        sleep(5)
        #确定提交
        self.login.driver.find_element_by_css_selector('.el-dialog__footer button:nth-child(2)').click()
        #提交成功之后，获取页面提示框信息
        loc = (By.CLASS_NAME,'el-message--success')
        WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(loc))
        msg = self.login.driver.find_element(*loc).text
        print("msg的值："+msg)
        print("保存成功！")
        assert msg == "保存成功！"
        assert username in self.login.driver.page_source

if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinSettings.py'])





