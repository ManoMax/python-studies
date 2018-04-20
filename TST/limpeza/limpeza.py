# coding: utf-8

servico = int(raw_input())

if servico == 1:
	tamanho = int(raw_input())
	preco = 80 * tamanho
	print "R$", str(preco) + ",00"
	if preco >= 200:
		print "Brinde!"
	
if servico == 2:
	tamanho = int(raw_input())
	preco = 50 * tamanho
	print "R$", str(preco) + ",00"
	if preco >= 200:
		print "Brinde!"
	
if servico == 3:
	print "R$ 50,00"
