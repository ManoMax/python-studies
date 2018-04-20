# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Imprime Primeira Vogal - CC (UFCG)

palavra = raw_input()
a = 'A'
e = 'E'
i = 'I'
o = 'O'
u = 'U'

for m in range(len(palavra)):
	letra = palavra[m]
	if letra.upper() in [a, e, i, o, u]:
		saida = letra
		break
	else:
		saida = "-"
print saida
