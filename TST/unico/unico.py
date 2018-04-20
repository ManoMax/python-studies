# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Único - CC (UFCG)

def unico(string):
	dados = []
	saida = ''
	for i in range(len(string)):
		if not string[i] in dados:
			saida += string[i]
			dados.append(string[i])
	return saida
	
assert unico("aa***xxxzzb+++") == "a*xzb+"
assert unico("") == ""
