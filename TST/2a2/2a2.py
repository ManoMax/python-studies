# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Inverte 2 a 2 condicional - CC (UFCG)

def inverte2a2_condicional(seq):
	for i in range(len(seq)-1):
		if i % 2 == 0:
			if seq[i] > seq[i+1]:
				aux = seq[i]
				seq[i] = seq[i+1]
				seq[i+1] = aux
	return seq

seq = [3, 1, 2, 3, 10, 5, 6]
inverte2a2_condicional(seq)
