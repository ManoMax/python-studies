import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
calcula_digitos_verificacao = getattr(undertest, 'calcula_digitos_verificacao', None)

class PublicTests(unittest.TestCase):

    def test_basico(self):
        assert calcula_digitos_verificacao('153245875') == '40'


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
