import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
seleciona_questoes = getattr(undertest, 'seleciona_questoes', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        todas = [1, 2, 3, 4, 5]
        utilizadas = [3, 4]
        seleciona_questoes(todas, utilizadas)
        assert todas == [1, 2, 5]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
