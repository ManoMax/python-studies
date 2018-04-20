# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Maior Palavra de Uma Frase - CC (UFCG)

def maior_palavra(phrase):
	larger = 0
	separate = phrase.split()
	for i in range(len(separate)):
		word = separate[i]
		cont = 0
		for i in range(len(word)):
			cont += 1
			if cont >= larger:
				larger = cont
				choice = word
	return choice

assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"
