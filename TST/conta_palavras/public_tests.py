import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
conta_palavras = getattr(undertest, 'conta_palavras', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
