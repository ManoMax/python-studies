# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Email Perdido - CC (UFCG)

def encontra_email_perdido(l1, l2):
	for i in range(len(l1)):
		if l1[i] not in l2:
			return l1[i]

l1 = ['oi', 'ola', 'paguei']
l2 = ['ola', 'paguei']
assert encontra_email_perdido(l1,l2) == 'oi'
