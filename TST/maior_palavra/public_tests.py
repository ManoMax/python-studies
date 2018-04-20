import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
maior_palavra = getattr(undertest, 'maior_palavra', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
