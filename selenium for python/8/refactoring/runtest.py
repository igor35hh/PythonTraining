import unittest
from homepage import HomePage
from basetest import BaseTestCase

class SearchProductTest(BaseTestCase):
    def testSearchForProduct(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('PureGear SoftTek for Samsung S8')
        self.assertLessEqual(1, search_results.product_count)
        product = search_results.open_product_page('PureGear SoftTek for Samsung S8+ - Black') 
        self.assertEqual('PureGear SoftTek for Samsung S8+ - Black', product.name)
        self.assertEqual('$17.35', product.price)
        print(product.stock_status)
        self.assertEqual('Only 1 left in stock (more on the way).', product.stock_status)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)