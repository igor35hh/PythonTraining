from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://comfy.ua/")
        
    #def test_account_link(self):
        #WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
        
        #account = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
        #account.click()
        
    def test_compare_products_removal_alert(self):
        
        self.driver.find_element_by_xpath("//a[@href='tel:+0-800-303-505']").click()

        alert = WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        alert_text = alert.text
        print(alert_text)

        #self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
        alert.accept()
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
    
        
        