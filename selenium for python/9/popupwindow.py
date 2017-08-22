from selenium import webdriver
import unittest
from time import sleep

class PopupWindowTest(unittest.TestCase):
    URL = "https://rawgit.com/upgundecha/learnsewithpython/master/pages/Config.html"
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_window_popup(self):
        driver = self.driver
        
        parent_window_id = driver.current_window_handle
        help_button = driver.find_element_by_id("helpbutton")
        
        sleep(1)
        
        help_button.click()
        driver.switch_to.window("HelpWindow")
        driver.close()
        driver.switch_to.window(parent_window_id)
        
        sleep(1)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)