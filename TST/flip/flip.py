# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Atividade: Flip / CC - UFCG

def flip(l1, i, j):
	for x in range(len(l1)):
		if x >= i and x <= j:
			l1[i], l1[j] = l1[j], l1[i]
			i += 1
			j -= 1

l1 = [1, 2, 3, 4, 5, 6, 7]
assert flip(l1, 2, 5) == None
assert l1 == [1, 2, 6, 5, 4, 3, 7]
