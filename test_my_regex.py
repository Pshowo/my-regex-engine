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
        self.assertEqual(compare_word('ap|apple'),  True)
        self.assertEqual(compare_word('le|apple'),  True)
        self.assertEqual(compare_word('a|apple'),  True)
        self.assertEqual(compare_word('.|apple'),  True)
        self.assertEqual(compare_word('apwle|apple'),  False)

        self.assertEqual(compare_word('^app|apple'),  True)
        self.assertEqual(compare_word('^a|apple'),  True)
        self.assertEqual(compare_word('^a.|apple'),  True)
        self.assertEqual(compare_word('^le|apple'),  False)
        self.assertEqual(compare_word('^apple|apple pie'),  True)

        self.assertEqual(compare_word('le$|apple'),  True)
        self.assertEqual(compare_word('.$|apple'),  True)
        self.assertEqual(compare_word('app$|apple'),  False)
        self.assertEqual(compare_word('apple$|tasty apple'),  True)
        
        self.assertEqual(compare_word('^apple$|apple'),  True)
        self.assertEqual(compare_word('^apple$|tasty apple'),  False)
        self.assertEqual(compare_word('^apple$|apple pie'),  False)
        
        self.assertEqual(compare_word('colou?r|color'),  True)
        self.assertEqual(compare_word('colou?r|colour'),  True)
        self.assertEqual(compare_word('colou?r|colouur'),  False)

        self.assertEqual(compare_word('colou*r|color'),  True)
        self.assertEqual(compare_word('colou*r|colour'),  True)
        self.assertEqual(compare_word('colou*r|colouur'),  True)
        self.assertEqual(compare_word('colou*r|colouuuuur'),  True)

        self.assertEqual(compare_word('colou+r|color'),  False)
        self.assertEqual(compare_word('colou+r|colour'),  True)
        self.assertEqual(compare_word('colou+r|colouur'),  True)
        self.assertEqual(compare_word('colou+r|colouur'),  True)
        self.assertEqual(compare_word('colou+r|colouuuuur'),  True)

        self.assertEqual(compare_word('col.*r|color'),  True)
        self.assertEqual(compare_word('col.*r|colour'),  True)
        self.assertEqual(compare_word('col.*r|colr'),  True)
        self.assertEqual(compare_word('col.*r|collar'),  True)
        self.assertEqual(compare_word('col.*r|collar'),  True)
        self.assertEqual(compare_word('col.*r$|colors'),  True)

        self.assertEqual(compare_word('.+|aaa'),  True)
        """
        self.assertEqual(compare_word('^no+pe$|noooooooope'),  True)
        self.assertEqual(compare_word('^n.+pe$|noooooooope'),  True)

        self.assertEqual(compare_word('\.$|end.'),  True)
        self.assertEqual(compare_word('3\+3|3+3=6'),  True)
        self.assertEqual(compare_word('\?|Is this working?'),  True)
        self.assertEqual(compare_word("\\|\\"),  True)
        self.assertEqual(compare_word("colou\?r|color"),  False)
        self.assertEqual(compare_word("colou\?r|colour"),  False)
    
        """

if __name__=="__main__":
    unittest.main()