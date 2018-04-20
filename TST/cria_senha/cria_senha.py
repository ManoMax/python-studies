# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Cria Senha - CC (UFCG)

def criaSenhaForte(palavra):
	saida = '(('
	for i in range(len(funcao)):
		if funcao[i].upper() == 'O':
			saida += '0'
		elif funcao[i].upper() == 'I':
			saida += '1'
		elif funcao[i].upper() == 'L':
			saida += '1'
		elif funcao[i].upper() == 'E':
			saida += '3'
		elif funcao[i].upper() == 'A':
			saida += '4'
		elif funcao[i].upper() == 'B':
			saida += '6'
		elif funcao[i].upper() == 'T':
			saida += '7'
		else:
			saida += funcao[i]
	saida += '))'
	return saida
		
while True:
	entrada = raw_input()
	dados = entrada.split()
	funcao = dados[0]
	if entrada == '***': break
	
	if dados[1] == 'fraco':
		saida = "((%s))" % dados[0]
		
	elif dados[1] == 'forte':
		saida = criaSenhaForte(funcao)
		
	print saida
