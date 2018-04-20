import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insere_ordenado_impostor = getattr(undertest, 'insere_ordenado_impostor', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l = [1, 2, 4, 3, 5, 6, 7, 11]
        insere_ordenado_impostor(l)
        assert l == [1, 2, 3, 4, 5, 6, 7, 11]

    def test_ex2(self):
        l = [1, 9, 11, 3, 14]
        insere_ordenado_impostor(l)
        assert l == [1, 3, 9, 11, 14]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
