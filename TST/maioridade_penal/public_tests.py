import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
maioridade_penal = getattr(undertest, 'maioridade_penal', None)

class PublicTests(unittest.TestCase):

    def test_basico_1(self):
        assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
