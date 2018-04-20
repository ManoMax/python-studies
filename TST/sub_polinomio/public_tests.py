import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
subtrai_polinomios = getattr(undertest, 'subtrai_polinomios', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        p1 = [-5, 4, 3]
        p2 = [-1, 0, 2, 0, 0, 0, 5]
        assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

    def test_exemplo_2(self):
        p1 = [-5, 4, 3]  # 3x2 + 4x - 5
        p2 = [-4, 2, 3]  # 3x2 + 2x - 4
        assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
