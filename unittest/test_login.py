import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # runs before all methods
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://automationpractice.com/index.php")
        assert "My Store" in cls.driver.title

    def setUp(self):
        # runs before each method
        self.driver.find_element_by_class_name("login").click()
        self.assertIn("Authentication", self.driver.page_source)

    def test_010_wrong_login_and_password(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test@test.com')
        pwd = driver.find_element_by_id('passwd')
        pwd.clear()
        pwd.send_keys('test111')
        driver.find_element_by_id('SubmitLogin').click()
        assert "Authentication failed." in driver.page_source

    def test_020_empty_password(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')  # use existing(valid) email
        driver.find_element_by_id('passwd').clear()
        driver.find_element_by_id('SubmitLogin').click()
        assert "Password is required." in driver.page_source

    def test_030_valid_login_and_password(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')
        pwd = driver.find_element_by_id('passwd')
        pwd.clear()
        pwd.send_keys('test1@3')
        driver.find_element_by_id('SubmitLogin').click()
        self.assertIn("My account", driver.page_source)

    # def tearDown(self):
    #    pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # suite = unittest.TestLoader().loadTestsFromTestCase(Login)
    # unittest.TextTestRunner(verbosity=2).run(suite)
