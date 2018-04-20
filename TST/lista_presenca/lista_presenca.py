# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Atividade: Lista Presença - CC (UFCG)

def cria_lista_presenca(turmas, nomes, num):
	presenca = []
	for i in range(len(turmas)):
		if num == turmas[i]:
			presenca.append(nomes[i])
	return presenca
	
turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
assert cria_lista_presenca(turmas, nomes, 5) == ["Carla", "Jose"]
