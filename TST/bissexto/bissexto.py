# coding: utf-8

ano = int(raw_input())

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
	print "%d é bissexto" % ano
else:
	print "%d não é bissexto" % ano
