from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



class Test_NaxinUserLogin(object):
    def setup_class(self):
        #启动chrome浏览器
        print("启动Chrome浏览器")
        self.driver = webdriver.Chrome()
        print(4444444444)
        #指定我们需要的页面
        self.driver.get('http://10.100.103.204:10001/dist/index.html#/login')
        #最大化窗口
        print("登录")
        self.driver.maximize_window()
        print("最大化")

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
    def test_user_login_ok(self):
        username = 'tanxiumei'
        pwd = '111111'
        expected = '南通智能污水处理站监控系统'
        # 定位输入用户名，并且输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(username)
        # 定位输入密码，并且输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys(pwd)
        # 定位点击登录，并且点击
        self.driver.find_element_by_class_name('el-button').click()
        #设置等待
        #验证登录之后的页面title和我们想要的title一致，一致表示登录成功
        sleep(3)
        assert self.driver.title == expected
        dd = self.driver
if __name__ == '__main__':
    pytest.main(['-sv','test_naxinuser.py'])
