# coding: utf-8
# Aluno: Samuel Lucas V. Matos
# Matricula: Nenhuma
# Questão: Maioridade Penal Função - CC (UFCG)

def maioridade_penal(names, ages):
	name = names.split()
	age = ages.split()
	result = ''
	
	for i in range(len(age)):
		if int(age[i]) >= 18:
			if result == '':
				result += name[i]
			else:
				result += ' ' + name[i]
	
	return result

assert maioridade_penal('Jansen Italo Ana', '14 21 60') == "Italo Ana"
