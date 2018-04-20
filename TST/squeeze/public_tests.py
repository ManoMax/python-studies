import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
squeeze= getattr(undertest, 'squeeze', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
      nums = [3, 1, 1, 1, 4, 7, 3, 3, 2, 7]
      assert squeeze(nums) == [3, 1, 4, 7, 3, 2, 7]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
