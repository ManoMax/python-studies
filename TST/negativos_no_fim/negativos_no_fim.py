# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Negativos no fim - CC (UFCG)

def negativos_no_fim(fila):
	cont = len(fila)-1
	for i in range(len(fila)-1, -1, -1):
		if fila[i] < 0:
			fila[i], fila[cont] = fila[cont], fila[i]
			cont -= 1

fila = [12, -21, -35, 8, 12, 15]
assert negativos_no_fim(fila) == None
assert fila == [12, 12, 15, 8, -21, -35]
