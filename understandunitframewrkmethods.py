import  unittest
def setUpModule():#Set up module  will execute once before executing any  class method in test class
    print("setup module")
def tearDownModule():#Tear down module  will execute once after executing  completing everthing in python module
    print("teardown module")
class AppTesting(unittest.TestCase):

    @classmethod    #decorator
    def setUp(self) -> None:
        print("this is login test")
    @classmethod
    def tearDown(self) -> None:
         print("this is logout test")
    @classmethod
    def setUpClass(cls) -> None:
        print("open app")
    @classmethod
    def tearDownClass(cls) -> None:
        print("close app")

    def test_search(self):
        print("this is test search")


    def test_advsearch(self):
        print("this is test adv search")

if __name__ == "__main__":
    unittest.main()