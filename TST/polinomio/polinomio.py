# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Valor Polinômio - CC (UFCG)

def valor_polinomio(poli, valor):
	result = 0
	x = len(poli)
	for i in range(len(poli)-1, -1, -1):
		if poli[i] != 0:
			result += int(poli[i]) * valor**i
	return result

assert valor_polinomio([-5, 0, 2, 0, 3], 2) == 51
