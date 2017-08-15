import unittest
from selenium import webdriver
from time import sleep

class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        
        self.driver.get("https://comfy.ua/")
        
    def test_register_new_user(self):
        pass
        driver = self.driver
        driver.find_element_by_link_text("Вход").click()
        sleep(1)
        #create_account_button = driver.find_element_by_link_text("Регистрация")
        create_account_button = self.driver.find_element_by_xpath("//span[@data-gtm='Interactions-open-registrationForm']")
        
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        
        sleep(1)
        
        first_name = driver.find_element_by_id("registration_name")
        phone_name = driver.find_element_by_id("registration_phone")
        email_address = driver.find_element_by_id("registration_email")
        submit_button = driver.find_element_by_xpath("//button[@data-gtm='Conversions-click-registr']")
        
        first_name.send_keys("Игорек")
        
        #phone_name.send_keys("+38(096)544-02-33")
        
        phone_name.send_keys("")
        phone_name.send_keys("0")
        phone_name.send_keys("9")
        phone_name.send_keys("6")
        phone_name.send_keys("5")
        phone_name.send_keys("4")
        phone_name.send_keys("4")
        phone_name.send_keys("0")
        phone_name.send_keys("2")
        phone_name.send_keys("3")
        phone_name.send_keys("3")
        
        #email_address.send_keys("igor@ua.fm")
        
        email_address.send_keys("i")
        email_address.send_keys("g")
        email_address.send_keys("o")
        email_address.send_keys("r")
        email_address.send_keys("@")
        email_address.send_keys("u")
        email_address.send_keys("a")
        email_address.send_keys(".")
        email_address.send_keys("f")
        email_address.send_keys("m")
        
        sleep(3)
        
        self.assertEqual("false", first_name.get_attribute("aria-invalid"))
        self.assertEqual("false", phone_name.get_attribute("aria-invalid"))
        #self.assertEqual("false", email_address.get_attribute("aria-invalid"))
        
        self.assertTrue(first_name.is_enabled() and phone_name.is_enabled() and
                        email_address.is_enabled(), submit_button.is_enabled())
        
        submit_button.click()
        
        sleep(3)
        
        title = 'На Ваш номер телефона был отправлен пароль в SMS/Viber. Пожалуйста введите его ниже'
        self.assertEqual(title, driver.find_element_by_id("enter_password_notification").text)
        
        #self.assertTrue(driver.find_element_by_xpath("//button[@data-gtm='Interactions-click-signIn']").is_displayed())
        self.assertTrue(driver.find_element_by_xpath("//button[@data-gtm='Interactions-click-signIn']").is_enabled())
        
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
        