import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
inverte3a3 = getattr(undertest, 'inverte3a3', None)

class PublicTests(unittest.TestCase):

    def test_3(self):
        assert inverte3a3("paisimtio") == "tiosimpai"

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
