# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Quem acertou menos - CC (UFCG)

n = int(raw_input())
soma = 0
maior_quantidade = 0
aluno = 1

for i in range(n):
	erros = raw_input()
	for j in range(len(erros)):
		if erros[j] == 'f':
			soma += 1
	if soma > maior_quantidade:
		maior_quantidade = soma
		aluno = i + 1
	soma = 0
if n == 0:
	aluno = 0

print "O aluno %d errou %d teste(s)." % (aluno, maior_quantidade)
