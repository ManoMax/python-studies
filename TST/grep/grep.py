# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Grep - CC (UFCG)

palavra = raw_input()
N = int(raw_input())

for i in range(N):
	frase = raw_input()
	for j in range(len(frase)):
		if (palavra[0] == frase[j] and
		    palavra[1] == frase[j+1] and
		    palavra[2] == frase[j+2]):
				print frase
				break
