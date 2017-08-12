import unittest
from hometest import HomeTests
from searchtestclassmethod import SearchTests
import os
import HtmlTestRunner

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_test = unittest.TestLoader().loadTestsFromTestCase(HomeTests)

suite_test = unittest.TestSuite([home_test, search_test])

result_dir = os.getcwd()
runner = HtmlTestRunner.HTMLTestRunner(output=result_dir)
runner.run(suite_test)
