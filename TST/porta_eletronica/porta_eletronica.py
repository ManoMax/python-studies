# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Porta Eletrônica - CC (UFCG)

register = []

while True:
	
	cont = 0
	entrada = raw_input().split()
	if entrada[0] == 'S': break	
	user = entrada[1]
	if entrada[0] == 'R':
		register.append(user[0])
	elif entrada[0] == 'P':
		for u in range(len(register)):
			if user[0] == register[u]:
				cont += 1
		print cont
		
