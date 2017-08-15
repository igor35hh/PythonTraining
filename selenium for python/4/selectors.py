import unittest
from selenium import webdriver
from time import gmtime, strftime, sleep
from selenium.webdriver.support.ui import Select

class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        self.driver.get("https://comfy.ua/")
        
    def test_phone_options(self):
        exp_options = ["ENGLISH", "FRENCH", "GERMAN"]

        act_options = []

        select_language = Select(self.driver.find_element_by_id("select-language"))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options: act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual("ENGLISH", select_language.first_selected_option.text)

        select_language.select_by_visible_text("German")

        self.assertTrue("store=german" in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)

    def test_store_cookie(self):
        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_visible_text("French")
        self.assertEqual("french", self.driver.get_cookie("store")["value"])

        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)
        
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
        