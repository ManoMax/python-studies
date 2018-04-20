import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
unico = getattr(undertest, 'unico', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       assert unico("aa***xxxzzb+++") == "a*xzb+"

   def test_string_vazia(self):
       assert unico("") == ""

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
