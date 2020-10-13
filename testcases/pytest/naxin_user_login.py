from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Te1stNaxinUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://10.100.103.204:10001/dist/index.html#/login')
        self.driver.maximize_window()

    '''
    # 测试用户登录，用户名错误
    def test_user_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '111111'
        expected = '请输入用户名'

        # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_class_name('el-button').click()

        # 等待提示框
        #WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        #alert = self.driver.switch_to.alert
        sleep(1)
        test_name = self.driver.find_element_by_class_name('el-form-item__error').text
        sleep(3)
        #验证
        assert test_name == expected
        print(test_name)
        print(expected)
        sleep(2)
        # self.driver.quit()
    '''
        # 测试用户登录成功

    def testcart(self):
        # 用户名为空
        username = 'wangzi'
        pwd = '111111'
        expected = '南通智能污水处理站监控系统'

        # 输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_class_name('el-button').click()
        # 等待提示框
        #WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        #验证
        print(111222)
        assert self.driver.title == expected
        sleep(5)
