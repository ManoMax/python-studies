# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Vogais Primeiro - CC (UFCG)

def vogais_primeiro(word):
	a, e, i, o, u = 'a', 'e', 'i', 'o', 'u'
	order = ''
	accumulator = []
	for i in range(len(word)):
		if word[i].lower() == a or word[i].lower() == e or word[i].lower() == i or word[i].lower() == o or word[i].lower() == u:
			order += word[i]
		else:
			accumulator.append(word[i])

	for i in range(len(accumulator)):
		order += accumulator[i]
	return order
	
assert vogais_primeiro('exemplo') == 'eeoxmpl'
assert vogais_primeiro('Programacao 1') == 'oaaaoPrgrmc 1'
