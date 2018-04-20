# coding: utf-8
# Aluno: Gabriel Matos
# Matricula: 117110060
# Atividade: Pares de Múltiplos

sequencia = raw_input().split()
relacao = int(raw_input())
inteiro = []
contador = 0

for i in sequencia:
	num = int(i)
	inteiro.append(num)

for num in range(0, len(inteiro)-1):
	if inteiro[num] * relacao == inteiro[num+1]:
		contador += 1
	if float(inteiro[num]) / relacao == inteiro[num+1]:
		contador += 1
print "%s par(es)" % contador
		
for num in range(0, len(inteiro)-1):

	if inteiro[num] * relacao == inteiro[num+1]:
		print inteiro[num], inteiro[num+1]
	if float(inteiro[num]) / relacao == inteiro[num+1]:
		print inteiro[num], inteiro[num+1]
