# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Acordes - CC (UFCG)

def acordes(m1, m2):
	m3 = []
	for i in range(len(m1)):
		m3.append(m1[i])

	for j in range(len(m2)):
		if m2[j] not in m3:
			m3.append(m2[j])
	return m3

m1 = ['c', 'd', 'dm']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
assert m1 == ['c', 'd', 'dm']
assert m2 == ['c', 'a']

m1 = ['c', 'd']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'a']
