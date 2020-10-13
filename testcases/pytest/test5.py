import pytest


class TestCase1(object):

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')


if __name__ == '__main__':
    pytest.main(['-s'])
