
import  unittest
from  selenium import webdriver
class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")  # chrome driver location

        #self.assertIsNone(driver) # vairable  doesn't contain any value
        #self.assertIsNotNone(driver)
        driver.get("https://www.google.com/")
        print("Title of the page is:" + driver.title)

        titleOfWebpage=driver.title
        #assert equal
        #self.assertEqual("Google",titleOfWebpage,"webpage titleisnot same")
        #self.assertNotEqual("Google",titleOfWebpage)
        self.assertTrue(titleOfWebpage =="Google")
        #self.assertFalse()
        list={"python","selenium","java"}
        self.assertIn("python",list) #if the value is in list or not
        #self.assertNotIn()
        #.assertGreater(100,10)
        #self.assertGreaterEqual()
        #self.assertLess()
        #self.assertLessEqual()


if __name__ == "__main__":
    unittest.main()