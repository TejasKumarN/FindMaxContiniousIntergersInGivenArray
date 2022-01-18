import unittest
from FindLongestContiniousIntegersLength import getMaxContiniousIntegersCount

class TestCase(unittest.TestCase):

   def test_empty_array(self):
       inputArray = []
       result = getMaxContiniousIntegersCount(inputArray, 0)
       self.assertEqual(result, 0)

   def test_wrong_array_length_compared_with_actual_array_length(self):
       inputArray = [1, 2, 3]
       result = getMaxContiniousIntegersCount(inputArray, 5)
       self.assertEqual(result, 3)

   def test_happy_case_all_integers_correct_count(self):
       inputArray = [1, 2, 1, 2, 3]
       result = getMaxContiniousIntegersCount(inputArray, 5)
       self.assertEqual(result, 3)

   def test_invalid_array_with_str_elemets(self):
       inputArray = ["1", "2", "3"]
       with self.assertRaises(TypeError):
           result = getMaxContiniousIntegersCount(inputArray, 5)
           self.assertEqual(result, 3)