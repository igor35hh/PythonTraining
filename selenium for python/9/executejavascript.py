from selenium import webdriver
import unittest
from time import sleep

class ExecuteJavaScriptTest(unittest.TestCase):
    URL = "https://www.amazon.com/"
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_search_by_category(self):
        search_field = self.driver.find_element_by_name("field-keywords")
        self.highlightElement(search_field)
        search_field.clear()
        
        sleep(2)
        
        self.highlightElement(search_field)
        search_field.send_keys("PureGear SoftTek for Samsung S8")
        search_field.submit()
        
        sleep(2)
        
        #products = self.driver.find_elements_by_css_selector("ul.s-result-list.s-col-1.s-col-ws-1.s-result-list-hgrid.s-height-equalized.s-list-view.s-text-condensed.s-item-container-height-auto > li")
        products = self.driver.find_elements_by_xpath("//div[@class='a-row s-result-list-parent-container']/ul/li")
        print(len(products))
        self.assertLessEqual(1, len(products))
        
    def highlightElement(self, element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "color: green; border: 7px solid green;")
        #self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element , "")
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)