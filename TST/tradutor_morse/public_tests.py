# coding: utf-8
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
tradutor_morse = getattr(undertest, 'tradutor_morse', None)

class PublicTests(unittest.TestCase):
    
    def test_1(self):
       assert tradutor_morse(['.--.', '-.--', '-', '....', '---', '-.']) == 'python'


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
