# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Desenhando uma Árvore de Natal - CC (UFCG)

n = int(raw_input())
camadas = (n + n) - 1

for i in range(n-1, -1, -1):
	espaco = i * " "
	cont = i + i
	vezes = camadas - cont
	bolas = vezes * 'o'
	arvore = espaco + bolas
	if i == n-1:
		base = arvore
	print arvore
print base
