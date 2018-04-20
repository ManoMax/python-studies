import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
meu_join = getattr(undertest, 'meu_join', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     assert meu_join("*", "abc") == "a*b*c"

   def test_exemplo1(self):
     assert meu_join("*", ["a", "b", "c"]) == "a*b*c"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
