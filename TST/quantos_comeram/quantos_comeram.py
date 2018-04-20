# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Quantos Comeram? - CC (UFCG)

def quantos_comeram(N, fila):
	soma = 0
	for i in range(len(fila)):
		if N >= fila[i]:
			soma += fila[i]
			N -= fila[i]
		else: break
	return soma

assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
