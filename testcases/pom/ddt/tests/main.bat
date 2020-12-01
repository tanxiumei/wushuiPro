pytest --alluredir=report/  test_naxinUser.py test6.py --clean-alluredir
allure generate report/ -o reportHtml --clean
