# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Questões para mt - CC (UFCG)

def seleciona_questoes(todas, util):
	j = 0
	while j <= len(util)-1:
		for i in range(len(todas)-1, -1, -1):
			if todas[i] == util[j]:
				todas.pop(i)
		j += 1

todas = [1, 2, 3, 4, 5]
util = [3, 4]
seleciona_questoes(todas, util)
assert todas == [1, 2, 5]

todas = [1, 2, 3, 4, 5]
util = []
seleciona_questoes(todas, util)
assert todas == [1, 2, 3, 4, 5]

todas = []
util = [1, 2]
seleciona_questoes(todas, util)
assert todas == []

todas = [1, 1, 1, 2]
util = [1]
seleciona_questoes(todas, util)
assert todas == [2]

todas = [2]
util = [1]
seleciona_questoes(todas, util)
assert todas == [2]
