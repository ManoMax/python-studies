# coding: utf-8
# Aluno: Samuel Lucas V. Matos
# Matricula: Nenhuma
# Questão: Lanche mais Pedido - CC (UFCG)

def lanchemaispedido(lista):
	igual = []
	for k in range(len(lista)):
		igual.append(0)

	for i in range(len(lista)):
		for j in range(len(lista)):
			if lista[i] == lista[j] and i != j:
				igual[i] += 1

	maior = 0
	melhor = -3
	print igual
	for x in range(len(igual)):
		if igual[x] > maior and igual[x] > (len(lista)/2):
			melhor = x
			maior = igual[x]
	if melhor == -3:
		saida = None
	else:
		saida = lista[melhor]
	print saida
	return saida
	
ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']
marcos = ['suco','coxinha','suco','misto','folhado']

assert lanchemaispedido(ines) == 'tapioca'
assert lanchemaispedido(marcos) == None
