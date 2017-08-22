from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from time import sleep

class DoubleClickTest(unittest.TestCase):
    URL = "http://api.jquery.com/dblclick/"
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_double_click(self):
        driver = self.driver
        frame = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        box = driver.find_element_by_tag_name("div")
        
        self.assertEqual("rgba(0, 0, 255, 1)", box.value_of_css_property("background-color"))
        
        ActionChains(driver).move_to_element(driver.find_element_by_tag_name("span")).perform()
        ActionChains(driver).double_click(box).perform()
        
        sleep(5)
        
        self.assertEqual("rgba(255, 255, 0, 1)", box.value_of_css_property("background-color"))
              
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)