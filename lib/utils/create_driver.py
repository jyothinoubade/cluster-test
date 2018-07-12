import pytest
from selenium.webdriver import Firefox, Chrome, Ie
def get_driver_instance():
    browser_type = pytest.config.option.type.lower()
    env= pytest.config.option.env.lower()
    if browser_type=='firefox':
        driver= Firefox('./browser_server/geckodriver.exe')
    elif browser_type== 'Chrome':
        driver = Chrome('./browser_server/chromedriver.exe')
    elif browser_type== 'Ie':
        driver= Ie('./browser_server/iedriver.exe')
    else:
        print('Invalid browser option')
    elif env== 'remote':
        print('Add feature for remote execution')
    else:
        Print('Invalid Env option')


