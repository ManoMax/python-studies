# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: A Primeira Letra em Caixa Alta - CC (UFCG)


def caixa_alta(frase):
	
	text = ''
	for i in range(len(frase)-1):
		if i == 0 and frase[1] != ' ':
			text += frase[0].upper()
		elif i == 0 and frase[1] == ' ':
			text += frase[0].lower()
		
		if frase[i] == ' ' and frase[i+2] != ' ':
			text += frase[i+1].upper()
		else:
			text += frase[i+1].lower()
	return text
	
assert caixa_alta("A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
