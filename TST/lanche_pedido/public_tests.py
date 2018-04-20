import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
lanchemaispedido = getattr(undertest, 'lanchemaispedido', None)

class PublicTests(unittest.TestCase):

   def test_exemplo_1(self):
    ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']
    assert lanchemaispedido(ines) == 'tapioca'
    

   def test_exemplo_2(self):
       marcos = ['suco','coxinha','suco','misto','folhado']
       assert lanchemaispedido(marcos) == None
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
