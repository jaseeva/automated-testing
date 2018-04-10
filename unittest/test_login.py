import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginAndRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/index.php")
        self.assertIn("My Store", self.driver.title)
        self.driver.find_element_by_class_name("login").click()

    def test_forgot_password_wrong_email(self):
        driver = self.driver
        assert "Authentication" in driver.page_source
        driver.find_element_by_link_text("Forgot your password?").click()
        form = driver.find_element_by_id('form_forgotpassword')
        assert form
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('tttest9876@test.com')
        mail.submit()
        res = driver.find_element_by_css_selector('div.alert.alert-danger')
        assert res

    def test_forgot_password_valid_email(self):
        driver = self.driver
        assert "Authentication" in driver.page_source
        driver.find_element_by_link_text("Forgot your password?").click()
        form = driver.find_element_by_id('form_forgotpassword')
        assert form
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')
        mail.submit()
        res = driver.find_element_by_css_selector('p.alert.alert-success')
        assert res

    def test_wrong_login_and_password(self):
        driver = self.driver
        assert "Authentication" in driver.page_source
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test@test.com')
        pwd = driver.find_element_by_id('passwd')
        pwd.clear()
        pwd.send_keys('test111')
        driver.find_element_by_id('SubmitLogin').click()
        assert "Authentication failed." in driver.page_source

    def test_empty_password(self):
        driver = self.driver
        assert "Authentication" in driver.page_source
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')  # use existing(valid) email
        driver.find_element_by_id('passwd').clear()
        driver.find_element_by_id('SubmitLogin').click()
        assert "Password is required." in driver.page_source

    def test_valid_login_and_password(self):
        driver = self.driver
        assert "Authentication" in driver.page_source
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')
        pwd = driver.find_element_by_id('passwd')
        pwd.clear()
        pwd.send_keys('test1@3')
        driver.find_element_by_id('SubmitLogin').click()
        assert "My account" in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
    #suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndRegister)
    #unittest.TextTestRunner(verbosity=2).run(suite)
