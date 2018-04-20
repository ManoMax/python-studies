# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Criptografando uma Senha - CC (UFCG)

palavra = raw_input()
senha = ""
cont = 0
senha += palavra[0]
for i in range(1, len(palavra)):
	letra = palavra[i]
	if letra.upper() == "A":
		letra = "4"
		cont += 1
	elif letra.upper() == "E":
		letra = "3"
		cont += 1
	elif letra.upper() == "I":
		letra = "1"
		cont += 1
	elif letra.upper() == "O":
		letra = "0"
		cont += 1
	senha += letra
print "%s (%d troca(s))" % (senha, cont)
