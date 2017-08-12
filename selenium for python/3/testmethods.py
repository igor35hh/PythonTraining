import unittest
from selenium import webdriver
from time import sleep

class HomeTestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://comfy.ua/")
        
    def test_search_text_field_max_length(self):
        search_field = self.driver.find_element_by_id("headerCompareLink")
        self.assertEqual("0", search_field.get_attribute("data-count"))
        
    def test_search_button_enabled(self):
        search_button = self.driver.find_element_by_class_name("header-search__btn")
        self.assertTrue(search_button.is_enabled())
        
    def test_my_account_link_is_displayed(self):
        account_link = self.driver.find_element_by_link_text("Вход") #Sign In
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        account_links = self.driver.find_elements_by_partial_link_text("Вход") #Sign In
        self.assertTrue(len(account_links), 2)
       
    def test_count_of_promo_banners_images(self):
        banner_list = self.driver.find_element_by_class_name("header-logo__link")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(1, len(banners))
        
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath("//img[@alt='Comfy - сеть магазинов бытовой техники и электроники']")
        self.assertTrue(vip_promo.is_displayed())
        
        enter_promo = self.driver.find_element_by_xpath("//a[@href='#headerLogin']")
        enter_promo.click()
        sleep(1)
        enter_pass = self.driver.find_element_by_xpath("//button[@class='btn btn_round btn_round-white btn_block login-block__btn']")
        self.assertEqual("Получить пароль", enter_pass.text)
        
        close_button = self.driver.find_element_by_xpath("//a[@class='fancybox-item fancybox-close']")
        close_button.click()
        sleep(1)
        
    def test_shopping_cart_status(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.cart-head")
        shopping_cart_icon.click()
        
        shopping_cart_status = self.driver.find_element_by_css_selector("span.header-cart__i")
        count = shopping_cart_status.get_attribute('data-count')
        self.assertEqual('0', count)
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
        
        
        
        