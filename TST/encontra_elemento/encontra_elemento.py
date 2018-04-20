# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Encontra elemento - CC (UFCG)

N = int(raw_input())
sequencia = raw_input().split()
x = 0

for i in range(len(sequencia)):
	num = int(sequencia[i])
	if num == N:
		x = 1
if x == 1:
	print "sim"
else:
	print "não"
