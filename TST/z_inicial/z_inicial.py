# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Z Inicial - CC (UFCG)

def z_inicial(lista):
	cont = 0
	for i in range(len(lista)):
		palavra = lista[i]
		for j in range(len(palavra)):
			if palavra[0].upper() == 'Z':
				cont += 1
				break
	return cont

lista = raw_input().split()
print z_inicial(lista)
