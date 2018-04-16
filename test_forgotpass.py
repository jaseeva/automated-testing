import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # runs before all methods
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # runs before each method
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        assert "Login - My Store" in driver.title
        driver.find_element_by_link_text("Forgot your password?").click()
        form = driver.find_element_by_id('form_forgotpassword')
        assert form

    def test_010_forgot_password_empty(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "div.alert-danger")))
        res = driver.find_element_by_css_selector('div.alert-danger')
        assert res
        #print(res.text)

    def test_020_forgot_password_wrong_email(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('tttest9876@test.com')
        mail.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "div.alert-danger")))
        res = driver.find_element_by_css_selector('div.alert-danger')
        assert res
        #print(res.text)

    def test_030_forgot_password_valid_email(self):
        driver = self.driver
        mail = driver.find_element_by_id('email')
        mail.clear()
        mail.send_keys('test123321@test.com')
        mail.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "p.alert-success")))
        res = driver.find_element_by_css_selector('p.alert-success')
        assert res
        #print(res.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
