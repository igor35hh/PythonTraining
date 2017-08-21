from basepage import BasePage
from basepage import InvalidPageException

class ProductPage(BasePage):
    _product_view_locator = 'span.a-size-large'
    _product_name_locator = 'span.a-size-large'
    _product_description_locator = 'div.a-section.a-spacing-mini'
    _product_stock_status_locator = 'div.feature > div.a-section.a-spacing-none > span.a-size-medium.a-color-price'
    _product_price_locator = 'span.a-size-medium.a-color-price'
    
    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)
        
    @property
    def name(self):
        return self.driver.find_element_by_css_selector(self._product_name_locator).text.strip()
    
    @property
    def description(self):
        return self.driver.find_element_by_css_selector(self._product_description_locator).text.strip()
    
    @property
    def stock_status(self):
        return self.driver.find_element_by_css_selector(self._product_stock_status_locator).text.strip()
    
    @property
    def price(self):
        return self.driver.find_element_by_css_selector(self._product_price_locator).text.strip()
    
    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(self._product_view_locator)
        except:
            raise InvalidPageException('Product page not loaded')