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

    def test_compare_word(self):
        self.assertEqual(compare_word('a|a'),  True)
        self.assertEqual(compare_word('.|a'),  True)
        self.assertEqual(compare_word( '|a'),  True)
        self.assertEqual(compare_word( '|'),  True)
        self.assertEqual(compare_word('a|'),  False)
        self.assertEqual(compare_word('a|b'),  False)
        self.assertEqual(compare_word('apple|apple'),  True)
        self.assertEqual(compare_word('.pple|apple'),  True)
        self.assertEqual(compare_word('appl.|apple'),  True)
        self.assertEqual(compare_word('.....|apple'),  True)
        self.assertEqual(compare_word('aplle|apple'),  False)
        self.assertEqual(compare_word('peach|apple'),  False)
        self.assertEqual(compare_word('|apple'),  True)
        self.assertEqual(compare_word('apple|'),  False)

if __name__=="__main__":
    unittest.main()