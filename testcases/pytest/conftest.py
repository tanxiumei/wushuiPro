import pytest

from testcases.basic.naxin_user_login import NaxinUserLogin

@pytest.fixture(scope='session')
def userlogin():
    login = NaxinUserLogin()
    login.test_user_login_ok()
    return login