class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self,args):  #эту штуку увидел в видосе Окулика
        return self.driver.find_element(*args)

    def open(self,url):
        self.driver.get(url)