import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
flip = getattr(undertest, 'flip', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [1, 2, 3, 4, 5, 6, 7]
        assert flip(l1, 2, 5) == None
        assert l1 == [1, 2, 6, 5, 4, 3, 7]
     
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
