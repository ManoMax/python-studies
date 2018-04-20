# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Inteiros Positivos Divisíveis

A = int(raw_input())
B = int(raw_input())
K = int(raw_input())

for i in range(1, K+1):
	if i % A == 0 and i % B ==0:
		print i
