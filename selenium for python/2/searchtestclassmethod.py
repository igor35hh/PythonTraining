from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("http://hotline.ua/")
        
    def test_search_by_category(self):

        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//a[@class='g_statistic']")
        #self.assertEqual(96, len(products), 'no category')
        self.assertLessEqual(2, len(products))
        
    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("Headphones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//a[@class='g_statistic']")
        #self.assertEqual(96, len(products), 'no products')
        self.assertLessEqual(1, len(products))
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
