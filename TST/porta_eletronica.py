# coding: utf-8
# Beatriz Alice Alves Santos Azevedo
# Matricula = 117110343
# Porta eletrônica

record = []

while True:
	option = raw_input().split()
	
	if option[0] == 'R':
		record.append(option[1])
		
	if option[0] == 'P':
		user = 0
		for register in record:
			if register[0] == option[1]:
				user += 1
		print user
	
	if option[0] == 'S':
		break

