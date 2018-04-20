import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
cesar = getattr(undertest, 'cesar', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        assert cesar("exemplo", 4) == "ibiqtps"
    
    def test_exemplo_2(self):
        assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
