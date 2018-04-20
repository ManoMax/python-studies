import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
busca = getattr(undertest, 'busca', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       seq = [10, 7, 8, 6, 2, 31, 12]
       assert busca(seq, 8) == 2
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
