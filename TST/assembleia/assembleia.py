# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Analytics Assembleia - CC (UFCG)

def conta_votos(votacoes, id_votacao):
	cont_yes = 0
	cont_no = 0
	for i in range(len(votacoes)):
		data = votacoes[i].split(',')
		if id_votacao == int(data[2]):
			if data[1] == 'sim':
				cont_yes += 1
			elif data[1] == 'nao':
				cont_no += 1
	return [cont_yes, cont_no]

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')

assert conta_votos(votacao, 543) == [3,2]
