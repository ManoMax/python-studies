# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Calcula DV - CC (UFCG)

n = raw_input()
soma_par = 0
soma_impar = 0
mult = 0

for i in range(len(n)):
	if i % 2 == 0:
		soma_par += int(n[i])
	else:
		soma_impar += int(n[i])
	mult = soma_par * soma_impar
	rest = mult % 11

if rest == 10:
	print "%s-X" % n
else:
	print "%s-%d" % (n, rest)
