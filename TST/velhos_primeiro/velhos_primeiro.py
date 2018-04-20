# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Mais Velhos Primeiro - CC (UFCG)

def idosos_inicio(fila):
	data = fila
	row = []
	below = []
	x = 1
	y = 0
	while True:
		new_smaller = 35
		if x == 1:
			for i in range(len(data)):
				if int(data[i]) > 35:
					row.append(int(data[i]))
				elif int(data[i]) == 35:
					y = 1
				else:
					below.append(int(data[i]))
		
		for i in range(len(below)):
			if below == []: break
			smaller = int(below[i])
			if smaller <= new_smaller:
				new_smaller = smaller

		x = 0
		if y == 1:
			row.append(35)
			y = 0
		if below != []:
			below.remove(new_smaller)
			row.append(new_smaller)
		else: break
	return row

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
print idosos_inicio(fila)
assert idosos_inicio(fila) == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

