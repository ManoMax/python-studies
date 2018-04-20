#!/usr/bin/env python
# coding: utf-8
import unittest
import sys
import imp

class PublicTests(unittest.TestCase):

    def test_simples(self):
        votacao = []
        votacao.append('uma,sim,543,joao,PPPP')
        assert conta_votos(votacao, 543) == [1,0]

    def test_exemplo(self):
        votacao = []
        votacao.append('uma,sim,543,joao,PPPP')
        votacao.append('uma,nao,543,marina,PPPP')
        votacao.append('uma,sim,5,joao,PPPP')
        votacao.append('uma,nao,543,julio,P')
        votacao.append('uma,sim,543,carlos,PBBBB')
        votacao.append('uma,sim,543,juliana,PP')
        votacao.append('uma,sim,99,joao,PPPP')

        assert conta_votos(votacao, 543) == [3,2]

if __name__ == '__main__':

    undertest = imp.load_source("undertest", sys.argv[-1])
    conta_votos = undertest.conta_votos
    del sys.argv[-1]
    unittest.main()
