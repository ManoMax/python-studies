# coding: utf-8

salario = float(raw_input())
empregador = salario * 0.12

if salario <= 1317.07:
	empregado = salario * 0.08
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % empregado
elif 1317.08 <= salario <= 2195.12:
	empregado = salario * 0.09
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % empregado
elif salario > 2195.12:
	empregado = salario * 0.11
	print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % empregador
	print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % empregado
