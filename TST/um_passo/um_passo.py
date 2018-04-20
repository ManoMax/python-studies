# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Atividade: Um Passo do Algoritmo BubbleSort / CC - UFCG

while True:
	entrada = raw_input()
	if entrada == 'fim': break
	seq = entrada.split()
	
	if len(seq) == 2:
		seq[0], seq[1] = seq[1], seq[0]
	
	if len(seq) >= 3 and len(seq) % 2 == 0:
		for i in range(0, len(seq)-1, 3):
			seq[i], seq[i+1] = seq[i+1], seq[i]
			seq[i+1], seq[i+2] = seq[i+2], seq[i+1]
		
	if len(seq) >= 3 and len(seq) % 2 == 1:
		for j in range(0, len(seq)-1, 3):
			if len(seq) - j <= 2:
				seq[j], seq[j+1] = seq[j+1], seq[j]
				break
			seq[j], seq[j+1] = seq[j+1], seq[j]
			seq[j+1], seq[j+2] = seq[j+2], seq[j+1]
			
	saida = ''
	for x in range(len(seq)):
		if x == len(seq)-1:
			saida += seq[x]
			break
		saida += seq[x] + ' '
	print saida
