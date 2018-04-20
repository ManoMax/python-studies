# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Subtração de Polinomios - CC (UFCG)

def subtrai_polinomios(p1, p2):
	p3 = []
	a = 0
	while True:
		if a <= len(p1)-1 and a <= len(p2)-1:
			b = p1[a] - p2[a]
		elif a <= len(p1)-1 and a > len(p2)-1:
			b = p1[a]
		elif a > len(p1)-1 and a <= len(p2)-1:
			b = - p2[a]
		elif a > len(p1)-1 and a > len(p2)-1:
			d = len(p3)-1
			if p3[d] == 0:
				p3.remove(0)
			return p3
		p3.append(b)
		a += 1

p1 = [-5, 4, 3]
p2 = [-1, 0, 2, 0, 0, 0, 5]
assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

p1 = [-5, 4, 3]
p2 = [-4, 2, 3]
assert subtrai_polinomios(p1, p2) == [-1, 2]
