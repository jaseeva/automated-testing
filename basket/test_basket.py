import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basket(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # runs before all methods
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def setUp(self):
        # runs before each method
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        assert "My Store" in driver.title
    '''
    def test_010_empty_cart(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@title = "View my shopping cart"]').click()
        assert "Your shopping cart is empty." in driver.page_source
    '''
    def test_020_add_item(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php?id_product=2&controller=product")
        WebDriverWait(driver, 10)
        driver.find_element_by_xpath('//*[@id="add_to_cart"]/button/span').click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "div.clearfix")))
        assert 'There is 1 item in your cart.' in driver.page_source

    def test_030_change_quantity(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@title = "View my shopping cart"]').click()
        total = driver.find_element_by_id('total_product_price_1_1_0')
        price = int(total.text[1:])
        driver.find_element_by_id('cart_quantity_up_1_1_0_0').click()
        WebDriverWait(driver, 10)
        print(total.text)
        assert int(total[1:]) == price * 2

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
