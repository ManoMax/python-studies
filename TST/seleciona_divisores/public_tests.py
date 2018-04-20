import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filtra_divisores = getattr(undertest, 'filtra_divisores', None)

class PublicTests(unittest.TestCase):


   def test_exemplo(self):
       lista1 = [333, 121, 81]
       assert filtra_divisores(lista1) == None
       assert lista1 == [333,81]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
