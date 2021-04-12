import unittest
from  selenium import webdriver
class SearchEnginesTest(unittest.TestCase):
    def test_Google(self): #initiate method
        self.driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  #chrome driver location
        self.driver.get("https://www.google.com/")
        print("Title of the page is:"+self.driver.title)
        self.driver.close()
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  # chrome driver location
        self.driver.get("https://www.bing.com/")
        print("Title of the page is:" + self.driver.title)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()
