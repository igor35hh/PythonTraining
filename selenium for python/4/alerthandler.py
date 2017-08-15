import unittest
from selenium import webdriver
from time import sleep
import selenium
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class AlertHandler(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        self.driver.get("https://comfy.ua/")
        
    def test_alert(self):
        
        self.driver.find_element_by_xpath("//a[@href='tel:+0-800-303-505']").click()
        
        sleep(1)
        
        windowids = self.driver.window_handles
        print(windowids)
        for h in windowids[1:]:
            self.driver._switch_to.window(h)
            self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        #WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        #alert = self.driver.switch_to_alert
        
        #alert = self.driver.switch_to.alert
        
        #print(alert.text)
        
        #self.driver.switch_to.alert.dismiss
        
        sleep(2)
       
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
        