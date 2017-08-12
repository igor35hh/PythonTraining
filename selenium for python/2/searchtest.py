from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("http://hotline.ua/")
        
    def test_search_by_category(self):

        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//a[@class='g_statistic']")
        self.assertEqual(96, len(products), 'no category')
        
    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("Headphones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//a[@class='g_statistic']")
        self.assertEqual(96, len(products), 'no products')
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
