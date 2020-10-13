import pytest

from testcases.basic.naxin_user_login import NaxinUserLogin

@pytest.fixture(scope='session')
def userlogin():
    print(111222)
    a = NaxinUserLogin()
    print(222222222222)
    a.test_user_login_ok()
    return a
