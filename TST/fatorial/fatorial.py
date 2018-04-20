# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Fatorial - CC (UFCG)

N = raw_input()
fatorial = int(N)
num = int(fatorial)

for i in range(int(N), 1, -1):
	num = int(fatorial)
	fatorial = num * (int(i)-1)
if int(N) == 0:
	fatorial = 1

print fatorial
