# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Insere Ordenado Impostor - CC (UFCG)

def insere_ordenado_impostor(l):
	troca = True
	while troca:
		for i in range(len(l)-1, -1, -1):
			print l[i], l[i-1]
			if l[i] < l[i-1]:
				l[i-1], l[i] = l[i], l[i-1]
				troca = False
				break
	print l
	return l

l = [1, 2, 4, 3, 5, 6, 7, 11]
insere_ordenado_impostor(l)
assert l == [1, 2, 3, 4, 5, 6, 7, 11]

l = [1, 9, 11, 3, 14]
insere_ordenado_impostor(l)
assert l == [1, 3, 9, 11, 14]
