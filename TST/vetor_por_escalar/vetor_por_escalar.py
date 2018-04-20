# coding: utf-8
# Aluno: Samuel Lucas V. Matos
# Matricula: Nenhuma
# Questão: Acordes - CC (UFCG)

def altera_vetor_por_escalar(vetor, escalar):
	for i in range(len(vetor)):
		vetor[i] = vetor[i] * escalar

vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]
