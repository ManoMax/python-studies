import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
calcula_seguro = getattr(undertest, 'calcula_seguro', None)

class PublicTests(unittest.TestCase):

    def test_basico(self):
        assert calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto']) == [120, "Risco Alto", 600.0]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
