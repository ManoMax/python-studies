import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
altera_vetor_por_escalar = getattr(undertest, 'altera_vetor_por_escalar', None)

class PublicTests(unittest.TestCase):

   def test_adicional_1(self):
       vetor_1 = [1, 2, 3]
       assert altera_vetor_por_escalar(vetor_1, -1) == None
       assert vetor_1 == [-1, -2, -3]
       assert altera_vetor_por_escalar(vetor_1, 2) == None
       assert vetor_1 == [-2, -4, -6]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
