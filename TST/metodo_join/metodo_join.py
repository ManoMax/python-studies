# coding: utf-8
# Aluno: Samuel Lucas V. Matos
# Matricula: Nenhuma
# Questão: Minha Implementação para o Método join - CC (UFCG)3

def meu_join(deli, seq):
	result = ''
	for i in range(len(seq)):
		if i == 0:
			result += seq[i]
		else:
			result += deli + seq[i]
	return result
	
assert meu_join('*', 'abc') == 'a*b*c'
assert meu_join('*', ["a", "b", "c"]) == 'a*b*c'
