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


class TestNaxinDispatch(object):
    def setup_class(self):
        self.login = NaxinUserLogin()

        self.login.test_user_login_ok()


    def testPatchList(self):
        print(1111111111)
        self.login.driver.find_element_by_xpath('//*[@id="/dispatchmanage"]').click()
        sleep(3)
        a = self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/table/thead/tr/th[1]')
        print(a.text)
        assert a.text=="序号"

    def testPatchList1(self):
        self.login.driver.find_element_by_xpath('//*[@id="/dispatchmanage"]').click()
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

    def testPatchChaxun(self):
        self.login.driver.refresh()
        sleep(2)
        self.login.driver.find_element_by_xpath('//*[@id="/dispatchmanage"]').click()
        sleep(1)

        ul = self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[1]/div/div/div').click()
        sleep(2)
        self.login.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
        # self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[8]/button').click()
        # self.testPatchList1()

        # 选择日期
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[4]/div/div/input').send_keys('2020-09-01')
        a = self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[6]/div/div/input').send_keys('2020-09-03')
        sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="/dispatchmanage"]').click()
        sleep(1)

        #

        # a = self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]').text
        # print(a)
        sleep(1)

    def testAddPatch(self):
        sleep(5)
        self.login.driver.refresh()
        sleep(3)
        # self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[7]/div/button').click()
        self.login.driver.find_element_by_xpath('//*[@id="/dispatchmanage"]').click()
        sleep(2)
        # 发起派单
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[8]/button').click()
        # 选择站点名称
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[1]/div/div/div').click()
        sleep(2)
        self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/ul/li[1]').click()
        sleep(2)
        self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/ul/li[1]').click()
        # 选择派单事项 /html/body/div[5]/div[1]/div[1]/ul/li[1]
        sleep(1)
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[2]/div/div/div').click()
        sleep(1)

        self.login.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
        sleep(1)
        # 选择指派人员 /html/body/div[6]/div[1]/div[1]/ul/li[1]
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div[3]/div/div').click()
        sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
        sleep(3)
        # 输入维修内容
        self.login.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/textarea').send_keys('申请设备维修')
        sleep(3)

        # 点击确定
        self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/button[2]').click()


if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinDispatch.py'])





