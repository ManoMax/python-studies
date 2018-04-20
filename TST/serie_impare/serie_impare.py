# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Série (ímpare 1) - CC (UFCG)

for i in range(1, 102, 2):
	num = i
	if i % 3 == 0:
		num = "*"
	if i % 5 == 0:
		num = "*"
	print num
