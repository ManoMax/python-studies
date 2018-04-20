import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
quantos_comeram = getattr(undertest, 'quantos_comeram', None)

class AcceptanceTests(unittest.TestCase):

    def test_exemplo(self):
        assert quantos_comeram(10, [10, 10]) == 10
        assert quantos_comeram(12, [10, 10]) == 10
        assert quantos_comeram(2, [10, 10]) == 0
        assert quantos_comeram(5, [2, 3, 5]) == 5

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
