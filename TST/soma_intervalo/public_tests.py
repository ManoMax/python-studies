import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
soma_intervalo = getattr(undertest, 'soma_intervalo', None)

class PublicTests(unittest.TestCase):

   def test_basico_1(self):
       assert soma_intervalo(10,10) == 10

   def test_basico_2(self):
       assert soma_intervalo(5,15) == 110

        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
