import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
idosos_inicio = getattr(undertest, 'idosos_inicio', None)


class AcceptanceTests(unittest.TestCase):

   def test_exemplo(self):
		fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
		self.assertEquals( idosos_inicio(fila), None )
		self.assertEquals( fila, [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34])

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
