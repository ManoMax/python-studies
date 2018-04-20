# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Agenda Ordenada - CC (UFCG)

nomes = []
while True:
	entrada = raw_input()
	if entrada == '####': break
	nomes.append(entrada)

ordem = []
for i in range(len(nomes)-2, -1, -1):
	nome = nomes[i]
	comp = nomes[i-1]
	for j in range(len(nome)+len(comp)):
		if nome[j] > comp[j]:
			aux = nomes[i]
			nomes[i] = nomes[i-1]
			nomes[i-1] = aux
			break
			
print nomes
