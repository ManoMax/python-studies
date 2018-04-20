import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
minmax_sort = getattr(undertest, 'minmax_sort', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     assert  minmax_sort([7, 4, 8, 1, 2, 3]) == [[1, 4, 3, 7, 2, 8], [1, 2, 3, 4, 7, 8], [1, 2, 3, 4, 7, 8]]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
