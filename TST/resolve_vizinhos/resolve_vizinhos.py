# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Matricula: 117110060
# Atividade: Resolve Vizinhos / CC - UFCG

def resolve_vizinhos(seq):
	troca = True
	while troca:
		troca = False
		
		for i in range(1, len(seq)-1):
			if seq[i] == seq[i-1]:
				seq[i-1] += 1
				
				if seq[i-1] == seq[i-2]:
					seq[i-1] += 1
				troca = True
	return seq
		
seq = [1,2,5,5,8,4]
assert resolve_vizinhos(seq) == [1,2,6,5,8,4]

seq = [1,6,5,5,8,4]
assert resolve_vizinhos(seq) == [1,6,7,5,8,4]

seq = [1,6,5,5,5,8,4]
assert resolve_vizinhos(seq) == [1,6,7,6,5,8,4]
