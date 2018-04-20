# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Make Set - CC (UFCG)

def make_set(l):
	for i in range(len(l)-1, -1, -1):
		a = len(l)-2
		print l
		while a >= 0:
			if l[i] == l[a]:
				l.pop(i)
			a -= 1
	print l

l = [2, 2, 2]
make_set(l)
assert l == [2]
