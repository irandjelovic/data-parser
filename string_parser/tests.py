#!/usr/bin/env python
'''
    String parser tests
'''


# standard lib
import unittest

# internal
from remove_adjacent_same_letters import remove_adjacent_same_letters, remove_adjacent_same_letters_recursion


class StringParserTest(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(remove_adjacent_same_letters(None), None)
        
    def test_no_input_recursion(self):
        self.assertEqual(remove_adjacent_same_letters_recursion(None), None)
        
    def test_one_letter(self):
        self.assertEqual(remove_adjacent_same_letters("a"), "a")
        
    def test_one_letter_recursion(self):
        self.assertEqual(remove_adjacent_same_letters_recursion("a"), "a")
        
    def test_two_letters(self):
        self.assertEqual(remove_adjacent_same_letters("aa"), "")
        
    def test_two_letters_recursion(self):
        self.assertEqual(remove_adjacent_same_letters_recursion("aa"), "")
        
    def test_more_than_two_letters(self):
        self.assertEqual(remove_adjacent_same_letters("adabbadab"), "b")
        
    def test_more_than_two_letters_recursion(self):
        self.assertEqual(remove_adjacent_same_letters_recursion("adabbadab"), "b")
        
    def test_symphony(self):
        self.assertEqual(remove_adjacent_same_letters("Sytuutmphoraarny"), "Symphony")
        
    def test_symphony_recursion(self):
        self.assertEqual(remove_adjacent_same_letters_recursion("Sytuutmphoraarny"), "Symphony")
        

if __name__ == "__main__":
    unittest.main()
        