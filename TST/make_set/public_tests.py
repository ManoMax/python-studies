import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
make_set = getattr(undertest, 'make_set', None)

class PublicTests(unittest.TestCase):

    def test_example(self):
        l = [1, 2, 1]
        make_set(l)
        assert l == [1, 2]

    def test_exemplo2(self):
        l = [1]
        make_set(l)
        assert l == [1]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
