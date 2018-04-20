import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
negativos_no_fim = getattr(undertest, 'negativos_no_fim', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        fila = [12, -21, -35, 8, 12, 15]
        assert negativos_no_fim(fila) == None
        assert fila == [12, 12, 15, 8, -21, -35]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
