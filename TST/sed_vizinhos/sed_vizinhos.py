# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Soma e Diminui Vizinhos! - CC (UFCG)

def soma_diminui_vizinhos(lista):
	if len(lista) == 0:
		return 0
	result = lista[0]
	for i in range(1, len(lista)):
		if i % 2 == 1:
			result += lista[i]
		elif i % 2 == 0:
			result -= lista[i]
	return result
	
lista = [1, 2, 3]
assert soma_diminui_vizinhos(lista) == 0
