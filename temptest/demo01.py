from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(1)
driver.find_element_by_id('kw').send_keys("selenium")
driver.find_element_by_id('su').click()
sleep(4)