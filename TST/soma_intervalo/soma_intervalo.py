# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: A Primeira Letra em Caixa Alta - CC (UFCG)

def soma_intervalo(a, b):
	soma = 0
	for i in range(a, b+1, 1):
		soma += i
	return soma

assert soma_intervalo(5, 15) == 110
assert soma_intervalo(10, 10) == 10
