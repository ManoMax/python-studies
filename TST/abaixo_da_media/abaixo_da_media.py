# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Abaixo da média - CC (UFCG)

N = raw_input()
sequencia = [N]
soma = int(N)
contador = 1.

while N != "fim":
	N = raw_input()
	if N != "fim":
		sequencia.append(N)
		soma += int(N)
		contador += 1.
		media = soma / contador
		
print "%.2f" % media

for i in range(len(sequencia)):
	if int(sequencia[i]) < media:
		print "%d %d" % (int(i+1), int(sequencia[i]))
