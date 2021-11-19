import unittest
from translator import french_to_english, english_to_french

"""Test File"""

class Testfrench_to_english(unittest.TestCase):
    """Test french_to_english""" 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'),'Hello') #Translate test
        self.assertEqual(french_to_english(''),'') #Null test
        self.assertNotEqual(french_to_english('pomme'),'pomme ') #Not equal test        

class Testenglish_to_french(unittest.TestCase):
    """Test english_to_french"""  
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour') #Translate test
        self.assertEqual(english_to_french(''),'') #Null test
        self.assertNotEqual(english_to_french('apple'),'apple ') #Not equal test     
        
unittest.main()
