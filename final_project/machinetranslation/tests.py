import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testHello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    def test_null(self):
        self.assertNotEqual(english_to_french(''), 'error')
    

class TestFrenchToEnglish(unittest.TestCase):
    def testBonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_null(self):
        self.assertNotEqual(french_to_english(''), 'error')

if __name__=="__main__":
    unittest.main()