import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
acordes = getattr(undertest, 'acordes', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        m1 = ['c', 'd', 'dm']
        m2 = ['c', 'a']
        
        assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
        assert m1 == ['c', 'd', 'dm']
        assert m2 == ['c', 'a']
        
        m1 = ['c', 'd']
        m2 = ['c', 'a']
        assert acordes(m1, m2) == ['c', 'd', 'a']


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
