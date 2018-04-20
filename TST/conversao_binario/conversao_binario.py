# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Conversão de Número na Base 2 para a Base 10 - CC (UFCG)

N = raw_input()
soma = 0

for i in range(len(N)-1, -1, -1):
	num = int(N[i-1])
	div = 256 / 2 * i
	if i == 8:
		div = 256
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 7:
		div = 128
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 6:
		div = 64
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 5:
		div = 32
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 4:
		div = 16
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 3:
		div = 8
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 2:
		div = 4
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 1:
		div = 2
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	elif i == 0:
		div = 1
		resultado = num * div
		print "%d * %d = %d" % (num, div, resultado)
	soma += resultado
print "%d(2) = %d(10)" % (int(N), soma)
