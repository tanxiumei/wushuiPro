
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

#from testcases.basic.naxinLogin import TestAdminLogin
#from testcases.basic.naxin_user_login import NaxinUserLogin
#from testcases.basic.naxin_user_login import NaxinUserLogin
#from testcases.pytest.naxin_user_login import TestNaxinUserLogin
import random

#获取csv文件里的内容，返回一个包含list的list
#from testcases.pom.ddt.pages.NaxinSettingsPage import NaxinSettingPage
#from testcases.pom.ddt.tests.test_naxinUser import TestnaxinUserLogin
from wushuiPro.testcases.pom.ddt.pages.NaxinSettingsPage import NaxinSettingPage
from wushuiPro.testcases.pom.ddt.tests.test_naxinUser import TestnaxinUserLogin
from wushuiPro.util.ctrExcelFile import getData


class TestNaxinSettings(object):
    def setup_class(self):
        self.login = TestnaxinUserLogin()
        print(self.login)
        print("tanxiumei")
        self.NaxinSettingsPage = NaxinSettingPage(self.login)


    @pytest.mark.dependency(depends=["tanxiumei"],scope='session')
    def test_DelUser(self):
        self.NaxinSettingsPage.click_settings()
        self.NaxinSettingsPage.click_delete()
        assert "南通智能污水处理站监控系统" == self.login.driver.title
        sleep(3)

    @pytest.mark.parametrize('listData',getData('testData.csv'))
    @pytest.mark.dependency(depends=["tanxiumei"], scope='session')
    def test_addUser(self,listData):
        name = listData[0]
        number = listData[1]
        username = listData[2]
        password = listData[3]
        picFile = listData[4]
        self.NaxinSettingsPage.click_settings()
        msg = self.NaxinSettingsPage.click_addUser(name,number,username,password,picFile)
        # 提交成功之后，获取页面提示框信息
        loc = (By.CLASS_NAME, 'el-message--success')
        print("msg的值：" + msg)
        print("保存成功！")
        #assert msg == "保存成功！"
        assert name in self.login.driver.page_source

    @pytest.mark.dependency(depends=["tanxiumei"], scope='session')
    def test_editUser(self):
        self.NaxinSettingsPage.click_settings()
        self.NaxinSettingsPage.click_edit('五月','15859685274','wuyeu','222222','C:\\Users\\dell\\Pictures\\mingxing\\huo.png')

    @pytest.mark.dependency(depends=["tanxiumei"],scope='session')
    def test_searchUser(self):
        self.NaxinSettingsPage.click_settings()
        self.NaxinSettingsPage.click_search("谈秀梅")
        assert 'tanxiumei' in self.login.driver.page_source
        assert "暂无数据" not in self.login.driver.page_source

    @pytest.mark.dependency(depends=["tanxiumei"], scope='session')
    def test_add_suit(self):
        suit_name = "无锡纳新科技"
        self.NaxinSettingsPage.click_add_suit(suit_name,2,33,'无锡市惠山区万达广场')
        assert suit_name in self.login.driver.page_source
    def test_edit_suit(self):
        self.NaxinSettingsPage.click_edit_suit("修改站点名",1,888,"测试地址")
    def test_search_suit(self):
        suit_name='维纳阳光'
        self.NaxinSettingsPage.click_search_suit(suit_name)
        #assert suit_name in self.login.driver.page_source
        print("page_source的值")
        #print(self.login.driver.page_source)
    def test_delete_suit(self):
        self.NaxinSettingsPage.click_delete_suit()
        assert "站点名" in self.login.driver.page_source
        print("删除成功")

    def test_to_waring(self):
        self.NaxinSettingsPage.click_edit_warning(2,5,4,8,11,22,99)
        assert  "99" in self.login.driver.page_source
    def teardown_class(self):
        sleep(10)
        pass
        #self.login.driver.quit()
if __name__ == '__main__':
    pytest.main(['-sv','test_NaxinSettings.py'])





