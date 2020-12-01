import random
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from testcases.pom.ddt.pages.basePage import BasePage
from wushuiPro.testcases.pom.ddt.pages.basePage import BasePage


class NaxinSettingPage(BasePage):

    def __init__(self,login):
        self.login = login
        BasePage.__init__(self,self.login.driver)
        self.login = login
        self.login.driver.implicitly_wait(5)

    #定位删除
    # 点击系统设置loc
    click_settings_loc = (By.XPATH,'//*[@id="/setmanage"]')
    #sleep(3)
    #点击删除loc
    click_delete_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/div/button[2]')
    #点击确认loc
    #sleep(3)
    click_confirm_loc = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')

    #定位添加用户页面
    #定位添加按钮
    click_add_btn_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[3]/button')
    #定位人员姓名
    click_name_text_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/d'
                                          'iv[1]/input')
    weixiuNum = random.randint(1,4)
    #定位人员职位
    click_zhiwei1_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/div[1]')
    click_zhiwei2_loc = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]')

    #定位手机号码
    click_phoneNum_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div[1]/input')

    #定位用户名
    click_username_text_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[4]/div/div[1]/input')
    #定位密码
    click_pwd_text_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div[1]/input')
    #定位头像
    click_pic_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[6]/div/div/div')
    click_pic_name_loc = (By.NAME,'file')
    #定位确认
    click_ok_confirm_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/button[2]')
    #定位保存信息
    save_loc = (By.CLASS_NAME, 'el-message--success')

    #定位编辑页面的元素
    #定位编辑
    editUser_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/div/button[1]')
    edit_name_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input')
    #定位职位
    edit_post_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/div/input')
    #定位职位
    edit_post2_loc = (By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[2]')
    #定位手机号码
    edit_number_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div/input')
    #定位用户名
    edit_username_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[4]/div/div/input')
    #定位密码
    edit_pwd_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div/input')
    # 定位头像
    edit_pic_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[6]/div/div/div/img')
    edit_pic_name_loc = (By.NAME, 'file')

    #定位搜索功能
    #定位人员姓名搜索输入框
    search_name_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[1]/div/div/input')
    search_post_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div[1]/form/div[2]/div/div/div[1]/input')
    search_post2_loc =(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[2]')

    #定位站点设置页面
    #定位添加站点页面
    switch_to_suit_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[1]/div/ul/li[2]')
    #添加站点按钮
    add_suit_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/form/div[2]/button')
    #站点名
    add_suitName_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div[1]/input')
    #所属父级
    add_fatherSuit_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/div/input')
    add_fatherSuit2_loc = (By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[1]')
    #日均排污量
    add_flow_day_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/input')
    #站点地址
    add_address_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/input')

    #确认按钮
    add_confirm_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[3]/div/button[2]')
    #定位站点搜索框
    search_suit_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div/div/input')
    #定位删除按钮
    delete_suit_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/button[3]')
    delete_confirm_suit_loc=(By.XPATH,'/html/body/div[3]/div/div[3]/button[2]')

    #定位站点编辑页面
    edit_suit_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/button[2]')
    #定位编辑页面中的站点名称
    edit_suit_name_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input')
    #定位编辑页面中的所属父级、
    edit_suit_father_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/div/input')
    edit_suit_father2_loc =(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li[2]')#第二个
    #定位编辑页面中的日均排污量
    edit_suit_flow_day_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/input')
    #定位编辑页面中的站点地址
    edit_suit_address_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/input')
    #定位编辑页面中的确认
    edit_suit_confirm_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[3]/div/div[3]/div/button[2]')

    #定位告警页面
    #定位告警设置页面
    switch_to_warning_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div/ul/li[3]')
    #定位PH值
    edit_PH_firt_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div[1]/div/div/div/input')
    edit_PH_last_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div[3]/div/div/div/input')
    #定位DO值
    edit_DO_first_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div[1]/div/div/div/input')
    edit_DO_last_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div[3]/div/div/div/input')
    #定位电导率
    edit_elec_first_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div[1]/div/div/div[1]/input')
    edit_elec_last_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/div[3]/div/div/div/input')
    #定位液位
    edit_water_level_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[4]/div/div[1]/input')
    #定位确定
    edit_warning_confirm_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/form/div[5]/div/button')


    #告警设置页面操作
    def click_edit_warning(self,ph_first,ph_last,do_first,do_last,elec_first,elec_last,water_level):
        self.click(*self.switch_to_warning_loc)
        #sleep(1)
        self.clear(*self.edit_PH_firt_loc)
        self.type_text(ph_first,*self.edit_PH_firt_loc)
        self.clear(*self.edit_PH_last_loc)
        self.type_text(ph_last,*self.edit_PH_last_loc)
        self.clear(*self.edit_DO_first_loc)
        self.type_text(do_first,*self.edit_DO_first_loc)
        self.clear(*self.edit_DO_last_loc)
        self.type_text(do_last,*self.edit_DO_last_loc)
        self.clear(*self.edit_elec_first_loc)
        self.type_text(elec_first,*self.edit_elec_first_loc)
        self.clear(*self.edit_elec_last_loc)
        self.type_text(elec_last,*self.edit_elec_last_loc)
        self.clear(*self.edit_water_level_loc)
        self.type_text(water_level,*self.edit_water_level_loc)
        self.click(*self.edit_warning_confirm_loc)
        #sleep(5)

    #站点设置页面操作——
    # 添加站点
    def click_add_suit(self,name,fathername,flow,address):
        self.click(*self.switch_to_suit_loc)
        self.click(*self.add_suit_loc)
        self.type_text(name,*self.add_suitName_loc)
        self.click(*self.add_fatherSuit_loc)
        self.click(*self.add_fatherSuit2_loc)
        self.type_text(flow,*self.add_flow_day_loc)
        self.type_text(address,*self.add_address_loc)
        self.click(*self.add_confirm_loc)
    #编辑站点
    def click_edit_suit(self,name,fathername,flow,address):
        self.click(*self.edit_suit_loc)
        sleep(1)
        self.clear(*self.edit_suit_name_loc)
        self.type_text(name,*self.edit_suit_name_loc)
        sleep(1)
        self.click(*self.edit_suit_father_loc)
        self.click(*self.edit_suit_father2_loc)
        sleep(1)
        self.clear(*self.edit_suit_flow_day_loc)
        self.type_text(flow,*self.edit_suit_flow_day_loc)
        sleep(1)
        self.clear(*self.edit_suit_address_loc)
        self.type_text(address,*self.edit_suit_address_loc)
        sleep(1)
        self.click(*self.edit_suit_confirm_loc)
    def click_search_suit(self,name):
    #查询站点
        self.type_text(name,*self.search_suit_loc)
        self.clear(*self.search_suit_loc)
        self.login.driver.refresh()
    #删除站点
    def click_delete_suit(self):
        self.click(*self.delete_suit_loc)
        self.click(*self.delete_confirm_suit_loc)


    #人员管理页面操作：
    # 点击系统设置
    def click_settings(self):
        self.click(*self.click_settings_loc)
    # 点击删除
    def click_delete(self):
        self.click(*self.click_delete_loc)
        self.click(*self.click_confirm_loc)
    #搜索功能
    def click_search(self,name):
        self.type_text(name,*self.search_name_loc)
        self.click(*self.search_post_loc)
        self.click(*self.search_post2_loc)
    #点击编辑
    def click_edit(self,name,number,username,password,picFile):
        self.click(*self.editUser_loc)
        self.clear(*self.edit_name_loc) #清空姓名
        self.type_text(name, *self.edit_name_loc)  # 修改姓名
        self.click(*self.edit_post_loc) #选择职位
        self.click(*self.edit_post2_loc)#选择职位
        self.clear(*self.edit_number_loc) #清空电话号码
        self.type_text(number,*self.edit_number_loc) #修改电话号码
        self.clear(*self.edit_username_loc) #清空用户名
        self.type_text(username,*self.edit_username_loc) #修改用户名
        self.type_text(password,*self.edit_pwd_loc) #修改密码
        self.type_text(picFile, *self.edit_pic_name_loc) #修改头像
        self.click(*self.click_ok_confirm_loc)  #点击确认

    #添加用户
    def click_addUser(self,name,number,username,password,picFile):
        self.click(*self.click_add_btn_loc)    #点击添加
        self.type_text(name, *self.click_name_text_loc) #输入名字
        self.click(*self.click_zhiwei1_loc) #选择职位
        self.click(*self.click_zhiwei2_loc) #选择职位
        self.type_text(number,*self.click_phoneNum_loc) #输入电话号码
        self.type_text(username, *self.click_username_text_loc)   #输入用户名
        self.type_text(password, *self.click_pwd_text_loc)     #输入密码
        #self.click(*self.click_pic_loc)
        self.type_text(picFile,*self.click_pic_name_loc)
        self.click(*self.click_ok_confirm_loc)    #点击确定

        #WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(*self.save_loc))
        msg = self.login.driver.find_element(*self.save_loc).text

        #self.login.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/form/div[6]/div/div/div')
        #self.login.driver.find_element_by_name("file").send_keys(picFile)
        return msg




