import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
caixa_alta = getattr(undertest, 'caixa_alta', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     assert caixa_alta("A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
