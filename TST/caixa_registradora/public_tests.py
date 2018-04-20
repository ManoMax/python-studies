# coding: utf-8
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
caixa_registradora = getattr(undertest, 'caixa_registradora', None)

class PublicTests(unittest.TestCase):
    
    def test_1(self):
       assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
