import pytest


@pytest.mark.dependency(name='cart')
def test_cart():
    print("添加到购物车")


@pytest.mark.dependency(depends=["cart"])
def test_order():
    print(111)
    '''
        def testddUser(self):
            print(1111111111)
            self.login.driver.find_element_by_xpath('//*[@id="/setmanage"]').click()
            sleep(3)
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[3]/button').click()
            sleep(3)
           # WebDriverWait(self.driver, 5).until(EC.alert_is_present())
           # frame = self.driver.switch_to.frame()
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/d'
                                              'iv[1]/input').send_keys("自动化f设备名称25")
            #se = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/div/div/div/input').click()
            #select = Select(se)
           # se2 = self.driver.find_element_by_xpath('//*[@id="cascader-menu-3700-0"]/div[1]/ul').click()
            #定位设备类型  /html/body/div[5]/div[1]/div[1]/ul/li[1]
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/div[1]').click()

            # 切换窗口：
            # 找到新窗口名字
            #newwindow = self.login.driver.window_handles[0]
            # 切换到新窗口
            #self.login.driver.switch_to.window(newwindow)/html/body/div[4]/div[1]/div[1]/ul/li[2]
            sleep(2)
            self.login.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
            sleep(1)
            #// *[ @ id = "cascader-menu-8804-0-0"]
            #定位手机号码
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div[1]/input').send_keys(13945859632)
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[4]/div/div[1]/input').send_keys('tantantan')
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div[1]/input').send_keys(111111)
            self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/button[2]').click()

            loc = (By.CLASS_NAME,'el-message--success')
            WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(loc))
            msg = self.login.driver.find_element(*loc).text
            print("msg的值："+msg)
            print("保存成功！")
            assert msg == "保存成功！"
        '''

if __name__ == '__main__':
    pytest.main(['-sv','temp.py'])