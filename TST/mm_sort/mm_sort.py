# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: MinMax Sort = Selection Sort Duplicado - CC (UFCG)

def copia(seq):
	copia = []
	for i in range(len(seq)):
		copia.append(seq[i])
	return copia

def minmax_sort(seq):
	cont = len(seq)
	saida = []
	for i in range(len(seq) / 2):
		maior = seq[i]
		menor = seq[i]
		up, down = False, False
		
		for j in range(i+1, len(seq)-i):
			aux = seq[j]
			if aux < menor:
				i_menor = j
				menor = aux
				down = True
			if aux >= maior:
				i_maior = j
				maior = aux
				up = True
				
		if down:
			seq[i], seq[i_menor] = seq[i_menor], seq[i]
		if up:
			seq[j], seq[i_maior] = seq[i_maior], seq[j] 
		cont -= 1
		saida.append(copia(seq))
	return saida
	
assert minmax_sort([7, 4, 8, 1, 2, 3]) == [[1, 4, 3, 7, 2, 8],
                                           [1, 2, 3, 4, 7, 8],
                                           [1, 2, 3, 4, 7, 8]]

