# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Limite de gastos - CC (UFCG)

limit = float(raw_input())

while True:
	soma = 0
	entrada = raw_input()
	if entrada == 'fim': break
	dados = entrada.split()
	for i in dados:
		soma += float(i)
	if len(dados) != 0:
		media = soma / len(dados)
		if media < limit / 2.: break
		elif media >= limit:
			print entrada
