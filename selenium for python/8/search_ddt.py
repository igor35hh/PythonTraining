import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
    
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://hotline.ua/")
        
    @data(("phones", 2), ("Headphones", 1))
    @unpack
    def test_search(self, search_value, expected_count):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        
        self.search_field.send_keys(search_value)
        self.search_field.submit()
        
        products = self.driver.find_elements_by_xpath("//a[@class='g_statistic']")
        self.assertLessEqual(expected_count, len(products))
    
    def tearDown(self):
        self.driver.quit()    
        
if __name__ == '__main__':
    unittest.main(verbosity=2)