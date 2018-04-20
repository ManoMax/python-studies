#!/usr/bin/env python
import unittest
import sys
import imp

class PublicTests(unittest.TestCase):

    def test_simples(self):
        lista = [1,2,3]
        assert soma_diminui_vizinhos(lista) == 0

    def test_vazio(self):
        lista = []
        assert soma_diminui_vizinhos(lista) == 0


if __name__ == '__main__':

    undertest = imp.load_source("undertest", sys.argv[-1])
    soma_diminui_vizinhos = undertest.soma_diminui_vizinhos
    del sys.argv[-1]
    unittest.main()
