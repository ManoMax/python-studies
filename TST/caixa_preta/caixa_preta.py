# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Caixa Preta Descartando Leituras - CC (UFCG)

cont1 = 0
cont2 = 0
cont3 = 0
while True:
	entrada = raw_input().split()
	for i in range(len(entrada)):
		peso = int(entrada[0])
		combustivel = int(entrada[1])
		altitude = int(entrada[2])
	cont1 += 1
	cont2 += 1
	cont3 += 1
	if peso < 0:
		print "dado inconsistente. peso negativo."
		cont1 -= 1
		cont2 -= 1
		cont3 -= 1
		break
	elif combustivel < 0:
		print "dado inconsistente. combustível negativo."
		cont2 -= 1
		cont3 -= 1
		break
	elif altitude < 0:
		print "dado inconsistente. altitude negativa."
		cont3 -= 1
		break
print "peso: %d\ncombustível: %d\naltitude: %d" % (cont1, cont2, cont3)
