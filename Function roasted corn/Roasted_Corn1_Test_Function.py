


from Roasted_Corn1_Function_Class import length_Calculator
from unittest import TestCase

class Roasted_Corn1_Test_Function(TestCase):

    def test_length_Calculator(self):
        text = input("enter a text: ")
	length = length_Calculator(text)
self.assertTrue(length)
print(length)
