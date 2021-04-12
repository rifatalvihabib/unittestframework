
import  unittest

class AppTesting(unittest.TestCase):


    @unittest.SkipTest    #decorater
    def test_search(self):
        print("this is test search")

    @unittest.skip("I am skipping this")
    def test_advsearch(self):
        print("this is test adv search")
    @unittest.skipIf(1==1,"1 equals yto 1")
    def test_mradvsearch(self):
            print("this is test adv adv search")

    def test_mrsearch(self):
        print("this is test mr search")

if __name__ == "__main__":
    unittest.main()