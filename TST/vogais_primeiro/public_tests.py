import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
vogais_primeiro = getattr(undertest, 'vogais_primeiro', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        assert vogais_primeiro("exemplo") == "eeoxmpl"
    
    def test_exemplo_2(self):
        assert vogais_primeiro("Programacao 1") == "oaaaoPrgrmc 1"
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
