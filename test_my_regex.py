import unittest
from my_regex import *

class test_regex(unittest.TestCase):

    def test_my_regex(self):
        self.assertEqual(my_regex('a|a'), True)
        self.assertEqual(my_regex('.|a'), True)
        self.assertEqual(my_regex( '|a'), True)
        self.assertEqual(my_regex( '|'),  True)
        self.assertEqual(my_regex('a|'),  False)
        self.assertEqual(my_regex('a|b'),  False)

if __name__=="__main__":
    unittest.main()