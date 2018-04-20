# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Busca Linear - CC (UFCG)

def busca(seq, valor):
	pos = -1
	for i in range(len(seq)):
		if seq[i] == valor:
			pos = i
			break
	return pos

seq = [8, 9, 2, 3, 6, 10, 7, 9]
assert busca(seq, 6) == 4
assert busca(seq, 4) == -1
assert busca(seq, 9) == 1
