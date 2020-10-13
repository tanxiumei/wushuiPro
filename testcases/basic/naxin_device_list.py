import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from testcases.basic.naxinLogin import TestAdminLogin
from testcases.basic.naxin_user_login import NaxinUserLogin


class NaxinTestArticle(object):
    def setup_class(self):
        print(11111100)
        self.login = TestAdminLogin()
        print(111111)
    # 测试添加文章
    @pytest.mark.dependency(depends=["admin_login"], scope="module")
    #@pytest.mark.parametrize('title, content, expected', article_data)
    def test_add_ok(self):
        self.login.driver.find_element_by_xpath('//*[@id="/devicemanage"]').click()
        print(2222222222)
        sleep(5)


