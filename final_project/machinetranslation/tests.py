import unittest
from translator import frenchToEnglish, englishToFrench


class TestFrenchtoEnglish(unittest.TestCase):
    def test_null(self):
        self.assertEqual(frenchToEnglish(None), '')

    def test_translate(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')


class TestEnglishtoFrench(unittest.TestCase):
    def test_null(self):
        self.assertEqual(englishToFrench(None), '')

    def test_translate(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
