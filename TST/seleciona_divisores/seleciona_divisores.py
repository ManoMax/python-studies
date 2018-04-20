# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Seleciona Divisores em uma Lista - CC (UFCG)

def filtra_divisores(lista):
	for i in range(len(lista)-1, -1, -1):
		num = str(lista[i])
		soma = 0
		for j in range(len(num)):
			soma += int(num[j])
		if lista[i] % soma != 0:
			lista.pop(i)
	
lista1 = [333, 121, 81]
assert filtra_divisores(lista1) == None
assert lista1 == [333,81]
