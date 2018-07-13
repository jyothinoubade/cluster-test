import unittest
from lib.ui.login_page import LoginPage
from lib.utils import create_driver

class TestLoginU154322(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_cpmponents_tc154322(self):
        #goto Login page
        self.login_page.wait_for_login_page_to_load()
        #Verify Placeholder username text box
        actual_placeholder = self.login_page.get_username_textbox().get_attribute('placeholder')
        print(actual_placeholder)
        expected_placeholder = "Username"
        assert actual_placeholder == expected_placeholder
        # Verify Placeholder for Password text box
        actual_placeholder_pwd = self.login_page.get_password_textbox().get_attribute('placeholder')
        print(actual_placeholder_pwd)
        expected_placeholder_pwd = "Password"
        assert actual_placeholder_pwd == expected_placeholder_pwd
        status = self.login_page.get_login_button().is_enabled()
        assert status == True