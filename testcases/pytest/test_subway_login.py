# -*- coding:utf-8 -*-
# @File      :test_subway_login.py
# @Time      :2020/12/1 11:38
# @Author    :吾月
# @Email     :757560315@qq.com
# @Software  :PyCharm
import pytest
from appium.webdriver import webdriver
from time import sleep
from selenium import webdriver


class TestNaxinUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://10.100.103.204:10003/dist/index.html#/login')
        self.driver.maximize_window()
        # 测试用户登录成功

    def test_cart(self):
        # 用户名为空
        username = 'tanxiaomei'
        pwd = '111111'
        expected = '地铁隧道'

        # 输入用户名

        self.driver.find_element_by_css_selector("[placeholder='用户名']").send_keys(username)
        # 输入密码
        #self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_css_selector("[type='password']").send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_css_selector('.el-button').click()
        # 等待提示框
        #WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        #验证
        print(111222)
        assert self.driver.title == expected
        sleep(5)

if __name__ == '__main__':
    pytest.main(['-sv','test_subway_login.py'])