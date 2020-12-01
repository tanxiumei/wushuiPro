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
import sys

from testcases.basic.naxin_user_login import NaxinUserLogin


class TestNaxinRecord(object):

    #查询运维记录列表内容
    def test_recordList(self,userlogin):
        self.login = userlogin
        print("111")
        sleep(3)
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(3)
        for i in range(8):
            a = self.login.driver.find_element_by_css_selector('thead tr th:nth-child('+str(i+1)+')')
            print(a.text)
            #assert a.text=="序号"

    #查询运维记录列表1
    #@pytest.mark.skip(reason="调试")
    def test_recordList1(self,userlogin):
        self.login = userlogin
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
    #临时的test
    def test_temp(self):
        import sys
        path = sys.path[1]
        path2 = path+r"\wushuiPro\util\weihu.xls"
        print(path2)
        #'.el-table__body-wrapper tbody tr:first-child>td:last-child button:nth-child(1)'

    @pytest.mark.skip(reason="调试")
    def test_operate(self,userlogin):
        self.login = userlogin
        self.login.driver.refresh()
        sleep(2)
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(1)
        #打印
        pp = self.login.driver.find_element_by_css_selector('.el-table__body-wrapper tbody tr:first-child>td:last-child button:nth-child(1)')
        assert pp.text == "打印"
        #详情
        self.login.driver.find_element_by_css_selector(
            '.el-table__body-wrapper tbody tr:first-child>td:last-child button:nth-child(2)').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('.dialog-footer button').click()
        sleep(1)
        #删除
        self.login.driver.find_element_by_css_selector(
            '.el-table__body-wrapper tbody tr:first-child>td:last-child button:nth-child(3)').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('.el-message-box__btns button:nth-child(2)').click()#确认删除
        sleep(1)


    #查询功能
    #@pytest.mark.skip(reason="调试")
    def test_recordChaxun(self,userlogin):
        self.login = userlogin
        self.login.driver.refresh()
        sleep(2)
        self.login.driver.find_element_by_id('/recordmanage').click()
        sleep(1)
        #选择维护记录类型
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(1)').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('#app~div.el-select-dropdown.el-popper ul li:nth-child(1)').click()#选中第一个
        sleep(1)
        #请选择运维人员
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(2)').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('body>div[x-placement] ul>li:nth-child(2)').click()#选中第一个人
        sleep(1)
        # 选择日期
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(3) input').send_keys('2020-9-10')
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(5) input').send_keys('2020-9-12')
        sleep(1)
        self.login.driver.find_element_by_id('/recordmanage').click()
        #重置按钮
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(6)').click()
        sleep(1)
        #导入功能
        root_path = sys.path[1]
        xls_path = root_path + r"\wushuiPro\util\weihu.xls"
        print(xls_path)
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(7)').click()
        sleep(1)
        self.login.driver.find_element_by_name('file').send_keys(xls_path)
        sleep(1)
        #导出功能
        self.login.driver.find_element_by_css_selector('.el-form.el-form--inline>div:nth-child(8)').click()
        sleep(1)
       # assert "详情" in self.login.driver.page_source
        sleep(1)

if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinRecord.py'])





