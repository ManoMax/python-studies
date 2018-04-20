import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
resolve_vizinhos = getattr(undertest, 'resolve_vizinhos', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
        seq = [6,2,4,4,9,1,0]
        resolve_vizinhos(seq)
        assert seq == [6,2,5,4,9,1,0]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
