# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Produto de Dois Somatórios - CC (UFCG)

numero = raw_input()
soma_par = 0
soma_impar = 0

for i in range(len(numero)):
	if i % 2 == 0:
		num = numero[i]
		soma_par += int(num)
	else:
		num = numero[i]
		soma_impar += int(num)
		
produto = soma_par * soma_impar
print "%05d" % produto
