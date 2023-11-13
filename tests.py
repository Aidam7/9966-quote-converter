import unittest

from quotes_to_9966 import replace_quotes

class TestReplaceQuotes(unittest.TestCase):
    def test_single_quote(self):
        text = '"Guido van Rossuma"'
        expected = '„Guido van Rossuma“'
        self.assertEqual(replace_quotes(text), expected)
    def test_double_quote(self):
        text = '"Guido "van" Rossuma"'
        expected = '„Guido ‚van‘ Rossuma“'
        self.assertEqual(replace_quotes(text), expected)

    def test_triple_quote(self):
        text = '"Python jest językiem programowania stworzonym przez "Guido "van" Rossuma" w 1991 roku."'
        expected = '„Python jest językiem programowania stworzonym przez ‚Guido »van« Rossuma‘ w 1991 roku.“'
        self.assertEqual(replace_quotes(text), expected)

    def test_no_quote(self):
        text = 'Python jest językiem programowania stworzonym przez Guido van Rossuma w 1991 roku.'
        expected = 'Python jest językiem programowania stworzonym przez Guido van Rossuma w 1991 roku.'
        self.assertEqual(replace_quotes(text), expected)
    def test_too_many_quotes(self):
        text = '"Python jest językiem programowania stworzonym przez "Guido "v"a"n" Rossuma" w 1991 roku."'
        expected = None
        self.assertEqual(replace_quotes(text), expected)
if __name__ == '__main__':
    unittest.main()