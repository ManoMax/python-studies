# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Questão: Falta um - CC (UFCG)

def encontra_rotulo_perdido(env, rec):
	for i in range(len(env)):
		if env[i] not in rec:
			return env[i]

l1 = ['skol', 'brahma', 'itaipava']
l2 = ['itaipava', 'brahma']
assert encontra_rotulo_perdido(l1,l2) == 'skol'
