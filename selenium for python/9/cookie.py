import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class CookiesTest(unittest.TestCase):
    URL = "https://www.amazon.com/"
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_store_cookie(self):
        driver = self.driver
        
        select_department = Select(self.driver.find_element_by_name("url"))
        print(select_department.first_selected_option.text)
        self.assertEqual("All Departments", select_department.first_selected_option.text)
        
        sleep(1)
        
        store_cookie = driver.get_cookie("store")
        print(store_cookie)
        self.assertEqual(None, store_cookie)
        
        select_department.select_by_visible_text("Alexa Skills")
        
        sleep(1)
        #store_cookie = driver.get_cookie("store")['value']
        store_cookie = driver.get_cookie("store")
        print(store_cookie)
        #self.assertEqual("Alexa Skills", store_cookie)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)