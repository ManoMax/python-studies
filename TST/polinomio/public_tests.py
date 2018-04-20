import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
valor_polinomio = getattr(undertest, 'valor_polinomio', None)

class PublicTests(unittest.TestCase):

    def test_basico(self):
        assert valor_polinomio([-5, 0, 2, 0, 3], 10) == 30195
        assert valor_polinomio([-5, 0, 2, 0, 3], 2) == 51
        assert valor_polinomio([-5, 0, 2, 0, 3], 0) == -5

    def test_basico_2(self):
        assert valor_polinomio([3, 1], 100) == 103
        assert valor_polinomio([3, 1], 8) == 11
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
