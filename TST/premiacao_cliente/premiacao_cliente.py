# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Premiação Cliente - CC (UFCG)

cont_joao = 0
cont_julio = 0
soma_joao = 0
soma_julio = 0

while True:
	entrada = raw_input()
	dados = entrada.split()
	if entrada == 'fim':
		print "Não houve vencedor."
		break
	nome = dados[0]
	valor = float(dados[1])
	if nome == 'joao':
		cont_joao += 1
		soma_joao += valor
	elif nome == 'julio':
		cont_julio += 1
		soma_julio += valor
	dados = []
	if cont_joao > 2:
		print "joao foi o vencedor. Comprou mais de duas vezes no período."
		break
	elif cont_julio > 2:
		print "julio foi o vencedor. Comprou mais de duas vezes no período."
		break
	if soma_joao >= 2000:
		print "joao foi o vencedor. Comprou mais R$ 2000.00 no período."
		break
	elif soma_julio >= 2000:
		print "julio foi o vencedor. Comprou mais R$ 2000.00 no período."
		break
