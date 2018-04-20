# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Remove Palavras com Letras Iguais Consecutivas - CC (UFCG)

def remove_consecutivas(lista):
	for i in range(len(lista)-1, -1, -1):
		p = lista[i].upper()
		for j in range(len(p)-1):
			if p[j].upper() == p[j+1]:
				lista.pop(i)

lista1 = ['arara', 'tv',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'tv',  'bacia']

lista1 = ['arara', 'arroba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'bacia']
