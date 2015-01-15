# Tester module for the Markov Chain text generator.
#
# Author: Keyan Pishdadian 1/15/2015

import unittest
from main import *

class TestSequenceFunctions(unittest.TestCase):
    
    def setUp(self):
        self.input_string = "the fox brown fox jumped over the brown fox"
        self.output_dictionary = {'the':[('fox', 3), ('brown', 2)],
                                  'fox':[('brown', 1), ('fox', 1), ('jumped', 2), ('over', 1), ('the', 1)],
                                  'brown':[('fox', 2), ('jumped', 1), ('over', 1)],
                                  'jumped':[('over', 1), ('the', 1), ('brown', 1)],
                                  'over':[('the', 1), ('brown', 1), ('fox', 1)]}
        
    def test_simple_tokenize(self):
        self.assertEqual(self.output_dictionary, make_markov_dict(self.input_string))
    
if __name__ == '__main__':
    unittest.main()

