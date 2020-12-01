import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait

#from testcases.pom.ddt.pages.adminLoginPage import AdminLoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

#from testcases.pom.ddt.pages.basePage import BasePage
#from testcases.pom.ddt.pages.naxinUser import NaxinUserLoginPage
#from util import util
from wushuiPro.testcases.pom.ddt.pages.naxinUser import NaxinUserLoginPage


@allure.feature("登录页面")
class TestnaxinUserLogin(object):

    admin_login_data=[
        ('tanxiumei', '111111', '南通智能污水处理站监控系统'),
    ]
    def setup_class(self) -> None:
        self.driver = webdriver.Chrome()
        self.naxinUser = NaxinUserLoginPage(self.driver)
        self.naxinUser.goto_admin_login_page()
    # 测试管理员登录验证码错误
    @allure.story("这是登录的测试用例")
    @pytest.mark.run(order=1) #设置该测试用例为第一个执行
    @pytest.mark.dependency(name="tanxiumei")
    @pytest.mark.parametrize('username,pwd,expected', admin_login_data)
    def test_admin_login(self, username, pwd,expected):
        self.naxinUser.input_username(username)
        self.naxinUser.input_pwd(pwd)
        #if captcha != '666':
         #   captcha = util.get_code(self.driver, 'captchaImg')
      #  self.naxinUser.input_captcha(captcha)
        self.naxinUser.click_admin_login_btn()
        assert expected == self.driver.title
        sleep(5)

if __name__ == '__main__':
    # pytest --alluredir=report/  test_naxinUser.py
    # allure generate report/ -o reportHtml --clean  #--clean用于在运行之前清空reportHtml目录。
    #pytest.main(['test_naxinUser.py'])
    pytest.main(['--alluredir', './reports', '05 pytest allure生成测试报告.py'])
