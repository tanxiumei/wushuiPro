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

    @pytest.mark.skip(reason="调试")
    def testPatchList(self,userlogin):
        self.login = userlogin
        list1= ["序号",'站点名','指派人','手机','维保事项','状态','指派时间','操作']
        self.login.driver.find_element_by_id("/dispatchmanage").click()
        sleep(3)
        for i in range(8):
            a = self.login.driver.find_element_by_css_selector('thead th:nth-child('+str(i+1)+')')
            print(a.text)
            assert a.text==list1[i]

    @pytest.mark.skip(reason="调试")
    def testPatchList1(self,userlogin):
        self.login = userlogin
        self.login.driver.find_element_by_id("/dispatchmanage").click()
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

    @pytest.mark.skip(reason="调试")
    def testPatchChaxun(self,userlogin):
        self.login = userlogin
        self.login.driver.refresh()
        sleep(2)
        #self.login.driver.implicity_wait(10)
        self.login.driver.find_element_by_id("/dispatchmanage").click()
        sleep(1)

        # ul = self.login.driver.find_element_by_css_selector(
        #      '.app-page-select>form>div:nth-child(1) input').click()
        sleep(2)
        #请选择派单状态
        self.login.driver.find_element_by_css_selector('.app-page-select>form>div:nth-child(1) input').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('#app~div:last-child ul li:nth-child(2)').click()
        sleep(1)
        #请选择运维人员
        self.login.driver.find_element_by_css_selector('.app-page-select>form>div:nth-child(2) input').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('#app~div:last-child ul li:nth-child(2)').click()
        sleep(1)
        #请选择运维项目
        self.login.driver.find_element_by_css_selector('.app-page-select>form>div:nth-child(3) input').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('#app~div:last-child ul li:nth-child(2)').click()
        sleep(1)

        # 选择日期
        self.login.driver.find_element_by_css_selector('input[placeholder="选择开始日期"]').send_keys('2020-09-01')
        a = self.login.driver.find_element_by_css_selector('input[placeholder="选择结束日期"]').send_keys('2020-09-03')
        sleep(1)
        self.login.driver.find_element_by_id("/dispatchmanage").click()
        sleep(1)

        #

        # a = self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]').text
        # print(a)
        sleep(1)
    #审批派单/显示派单详情/删除派单三个一起
    def test_examinePatch(self,userlogin):
        self.login = userlogin
        self.login.driver.refresh()
        sleep(2)
        self.login.driver.find_element_by_id("/dispatchmanage").click()
        sleep(1)
        for i in range(3):
            print(i+1)
            self.login.driver.find_element_by_css_selector(
                'tbody tr:nth-child(1) td:last-child button:nth-child('+str(i+1)+')').click()
            sleep(3)
            if i==0:
                try:
                    sleep(1)
                    self.login.driver.find_element_by_css_selector('.el-message-box__btns button:last-child').click()
                    sleep(3)
                except:
                    print("已经审核过了，元素不能点击")
            elif i==1:
                self.login.driver.find_element_by_css_selector('[aria-label="派单详情"]>div:nth-child(3) button').click()
                sleep(3)
            else:
                self.login.driver.find_element_by_css_selector('.el-message-box__btns button:last-child').click()
                sleep(3)

    #@pytest.mark.skip(reason="调试")
    def testAddPatch(self,userlogin):
        self.login = userlogin
        sleep(5)
        self.login.driver.refresh()
        sleep(3)
        self.login.driver.find_element_by_id("/dispatchmanage").click()
        sleep(2)
        # 发起派单
        self.login.driver.find_element_by_css_selector('.app-page-select>form>div:nth-child(8) span').click()
        # 选择站点名称
        sleep(1)
        self.login.driver.find_element_by_css_selector('.el-form-item-inlines>div:nth-child(1) input').click()
        sleep(2)
        # self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/ul/li[1]').click()
        self.login.driver.find_element_by_css_selector('.el-popper.el-cascader__dropdown ul li:nth-child(1)').click()
        sleep(2)
        self.login.driver.find_element_by_css_selector('.el-cascader-panel>div:nth-child(2) ul li:nth-child(1)').click()
        # 选择派单事项 /html/body/div[5]/div[1]/div[1]/ul/li[1] cascader-menu-8491-0-0
        sleep(1)
        self.login.driver.find_element_by_css_selector('.el-form-item-inlines>div:nth-child(2) input').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('.el-popper.el-cascader__dropdown+div ul li:nth-child(1)').click()
        sleep(1)
        # 选择指派人员
        self.login.driver.find_element_by_css_selector('.el-form-item-inlines>div:nth-child(3) input').click()
        sleep(1)
        self.login.driver.find_element_by_css_selector('body.el-popup-parent--hidden>div:last-child ul li:nth-child(1)').click()
        sleep(3)
        # 输入维修内容
        self.login.driver.find_element_by_css_selector(
            'textarea.el-textarea__inner').send_keys('申请设备维修')
        sleep(3)

        # 点击确定
        self.login.driver.find_element_by_css_selector('.el-dialog__body+div div button:nth-child(2)').click()


if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinDispatch.py'])





