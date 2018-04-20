import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
encontra_email_perdido = getattr(undertest, 'encontra_email_perdido', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = ['oi', 'ola', 'paguei']
        l2 = ['ola', 'paguei']
        assert encontra_email_perdido(l1,l2) == 'oi'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
