
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://hotline.ua/")

search_field = driver.find_element_by_name("q")
search_field.clear()

search_field.send_keys("phones")
search_field.submit()

products = driver.find_elements_by_xpath("//a[@class='g_statistic']")

print('Found ' + str(len(products)) + ' products')

import sys
import locale
print(sys.getdefaultencoding())
print(locale.getpreferredencoding())
print(sys.stdout.encoding)

for product in products:
    row = product.get_attribute('title')
    print(row.encode('utf8')) #utf8, cp1251, cp866, koi8-r
    #print(bytes(row), 'utf-8')

    
driver.quit()

