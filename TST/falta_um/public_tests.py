import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
encontra_rotulo_perdido = getattr(undertest, 'encontra_rotulo_perdido', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = ['skol', 'brahma', 'itaipava']
        l2 = ['itaipava', 'brahma']
        assert encontra_rotulo_perdido(l1,l2) == 'skol'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
