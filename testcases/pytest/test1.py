import pytest


# 不会执行，不符合命名规则
def add():
    assert (1 + 2) == 3


def test_sub():
    assert 2 - 1 == 1


class TestRegister(object):
    def test_register(self):
        print(11111111111)
        assert len('admin') == 4


if __name__ == '__main__':
    # pytest.main(['-s', '-v', '01-pytest简介.py::test_sub'])
    # pytest.main(['-s', '-v', 'test1.py::TestRegister::test_register'])
    pytest.main(['-s', '-v', 'test1.py'])
