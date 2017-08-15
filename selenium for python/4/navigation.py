import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        self.driver.get("http://www.google.com")
        
    def test_browser_navigation(self):
        
        search_field = self.driver.find_element_by_name("q")
        search_field.clear()
        
        #sleep(1)
        
        search_field.send_keys("selenium webdriver")
        search_field.submit()
        
        #sleep(1)
        
        se_wd_link = self.driver.find_element_by_link_text("Selenium WebDriver")
        se_wd_link.click()
        self.assertEqual("Selenium WebDriver", self.driver.title)
        
        #sleep(1)
        
        self.driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("selenium webdriver - Поиск в Google")))
        
        self.driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))

        self.driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium WebDriver")))
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
        