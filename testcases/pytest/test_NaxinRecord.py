import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import unittest
import pytest

from testcases.basic.naxin_user_login import NaxinUserLogin


class TestNaxinRecord(object):
    def setup_class(self):
        self.login = NaxinUserLogin()
        self.login.test_user_login_ok()

    def test_recordList(self):
        print("运维记录页面测试用例")
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(3)
        a = self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/table/thead/tr/th[1]')
        print(a.text)
        assert a.text=="序号"

    def test_recordList1(self):
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(1)
        #获取表头的内容
        row = self.login.driver.find_elements_by_tag_name('tr')
        list = []
        for i in row:
            j = i.find_elements_by_tag_name('th')
            for item in j:
                text = item.text
                list.append(text)
        #print(list)
        #获取表格的内容
        list2 = []

        for x in row:
            y = x.find_elements_by_tag_name('td')
            list3 = []
            for item1 in y:
                text1 = item1.text
                #print(text1)
                list3.append(text1)
            #print(list3)
            if(list3!=[]):
                list2.append(list3)
            list3 = []
        print(list2)
        assert len(list2) != []


    def test_recordChaxun(self):
        self.login.driver.refresh()
        sleep(2)
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(1)
        # 选择日期
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[3]/div/div/input').send_keys('2020-09-01')
        a = self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[5]/div/div/input').send_keys('2020-09-30')
        sleep(1)
        self.login.driver.find_element_by_id('/recordmanage').click()
        assert "详情" in self.login.driver.page_source
        sleep(1)

if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinRecord.py'])





