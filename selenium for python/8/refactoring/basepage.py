from abc import abstractmethod

class BasePage():
    def __init__(self, driver):
        self._validate_page(driver)
        self.driver = driver
        
    @abstractmethod
    def _validate_page(self, driver):
        return
    
    @property
    def search(self):
        from searchbase import SearchRegion
        return SearchRegion(self.driver)
    
class InvalidPageException(Exception):
    pass