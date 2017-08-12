from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomeTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://comfy.ua/")
        
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'), 'no q element by name')
        
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'languageSwitcher'), 'no languageSwitcher element by id')
        
    def test_shoping_cart_empty_message(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.cart-head")
        shopping_cart_icon.click()
        
        shopping_cart_status = self.driver.find_element_by_css_selector("span.header-cart__i")
        count = shopping_cart_status.get_attribute('data-count')
        self.assertEqual('0', count)
        
        #close_button = self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        #close_button.click()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
