# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Calculadora - CC (UFCG)

while True:
	funcao = raw_input().split()
	for i in range(len(funcao)):
		if int(funcao[0]) == 1:
			x = int(funcao[1])
			y = int(funcao[2])
			adicao = x + y
			print adicao
			break
		if int(funcao[0]) == 2:
			x = int(funcao[1])
			y = int(funcao[2])
			sub = x - y
			print sub
			break
		if int(funcao[0]) == 3:
			x = int(funcao[1])
			y = int(funcao[2])
			mult = x * y
			print mult
			break
		if int(funcao[0]) == 4:
			x = int(funcao[1])
			y1 = int(funcao[2])
			if y1 == 0:
				div = "Erro: Divisão por 0"
			else:
				div = x / y1
			print div
			break
	if int(funcao[0]) == 5:
		break
