from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

class HomeTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://www.amazon.com/")
        
    def test_search_field(self):
        
        search_field = self.driver.find_element_by_name("field-keywords")
        search_field.clear()
        
        search_field.send_keys("PureGear SoftTek for Samsung S8")
        search_field.submit()
        
        sleep(1)
        
        #_product_list_locator = 'div.a-row.s-result-list-parent-container > ul > li'
        _product_list_locator = 'ul.s-result-list.s-col-1.s-col-ws-1.s-result-list-hgrid.s-height-equalized.s-list-view.s-text-condensed.s-item-container-height-auto > li'
        results = self.driver.find_elements_by_css_selector(_product_list_locator)
        print(len(results))
        
        _products = {}
        
        _product_name_locator = 'div.a-row.a-spacing-small > div > a > h2'
        _product_image_link = 'div.a-row.a-spacing-small > div > a'
        _page_title_locator = ''
        _products_count = 0
        
        for product in results:
            #row = product.get_attribute('title')
            #href = product.get_attribute('href')
            #print(row.encode('utf8'), href)
            
            name = product.find_element_by_css_selector(_product_name_locator).text
            print(name)
            _products[name] = product.find_element_by_css_selector(_product_image_link)
            
        print(_products)  
        #product.find_element_by_css_selector(_product_image_link).click()
        _products['PureGear SoftTek for Samsung S8+ - Black'].click()
        sleep(2)    
            
            
            
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
