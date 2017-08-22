import unittest
from selenium import webdriver
from castro import Castro #only for 2.6 python

class SearchProductTest(unittest.TestCase):
    URL = "https://www.amazon.com/"
    
    def setUp(self):
        self.screenCapture = Castro(filename="testSearchByCategory.swf")
        self.screenCapture.start()
        
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
    def test_search_by_category(self):
        search_field = self.driver.find_element_by_name("field-keywords")
        search_field.clear()
        
        search_field.send_keys("PureGear SoftTek for Samsung S8")
        search_field.submit()
        
        products = self.driver.find_elements_by_xpath("//div[@class='a-row s-result-list-parent-container']/ul/li")
        print(len(products))
        self.assertLessEqual(1, len(products))
        
    def tearDown(self):
        self.driver.close()
        self.screenCapture.stop()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)