# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Organiza Lista pela Média- CC (UFCG)

def organiza_por_media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    if len(lista) != 0:
        media = float(soma)/len(lista)
        j = 0
        k = 0
        while j < len(lista)-k:
            if lista[j] > media:
                lista.append(lista[j])
                lista.pop(j)
                k += 1
            else:
                j += 1

    return lista
		
p1 = [1,2,4,1,3,4,56,7,7,4,3,67]
assert organiza_por_media(p1) == [1,2,4,1,3,4,7,7,4,3,56,67]

p1 = [0]
assert organiza_por_media(p1) == [0]
