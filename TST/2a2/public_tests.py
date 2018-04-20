#!/usr/bin/env python
import unittest
import sys
import imp

class PublicTests(unittest.TestCase):

    def test_simples(self):
        seq = [3,1,2,3,10,5,6]                  
        inverte2a2_condicional(seq)
        assert seq == [1,3,2,3,5,10,6]

    def test_2(self):
        seq = [5,4,3,2,1]
        inverte2a2_condicional(seq)
        assert seq == [4,5,2,3,1]

if __name__ == '__main__':

    undertest = imp.load_source("undertest", sys.argv[-1])
    inverte2a2_condicional = undertest.inverte2a2_condicional
    del sys.argv[-1]
    unittest.main()
