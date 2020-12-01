from time import sleep

from selenium.webdriver.common.by import By

from wushuiPro.testcases.pom.pages.basePage import BasePage


class NaxinUserLoginPage(BasePage):

    username_input = (By.NAME, 'user')
    username_input2 = (By.XPATH,'//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input')
    pwd_input = (By.NAME, 'pwd')
    pwd_input2 =(By.XPATH,'//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
    captcha_input = (By.NAME, 'captcha')
    register_btn = (By.CLASS_NAME, 'btn')
    register_btn2 = (By.CLASS_NAME,'el-button')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_admin_login_page(self):
        self.driver.get('http://10.100.103.204:10001/dist/index.html#/login')
        self.driver.maximize_window()

    def input_username(self, username):
        self.clear(*self.username_input2)
        self.type_text(username, *self.username_input2)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input2)
        self.type_text(pwd, *self.pwd_input2)

    #def input_captcha(self, captcha):
     #   self.clear(*self.captcha_input)
      #  self.type_text(captcha, *self.captcha_input)

    def click_admin_login_btn(self):
        self.click(*self.register_btn2)
        sleep(2)


