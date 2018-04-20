# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matrícula: 117110060
# Atividade: Descarta Coincidentes

quantidade = int(raw_input())
valores = []
descartados = []
aceitos = []
contadorD = 0
contadorA = 0

for i in range(quantidade):
	valores.append(raw_input())
print "---"

for numero in range(len(valores)):
	individual = valores[numero]
	aceitos.append(individual)
	for algarismo in range(len(individual)):
		if int(algarismo) == int(individual[algarismo]):
			descartados.append(individual)
			aceitos.remove(individual)
			contadorD += 1
			break
contadorA = quantidade - contadorD
			
print "%d aceito(s)" % contadorA
for i in aceitos:
	print i
print "%d descartado(s)" % contadorD
for i in descartados:
	print i
