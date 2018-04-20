# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Conta Palavras - CC (UFCG)

def conta_palavras(num, entrada):
	entrada = entrada.split(':')
	cont = 0
	for i in range(len(entrada)):
		if len(entrada[i]) >= num:
			cont += 1
	return cont
	
assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
