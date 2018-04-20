# coding: utf-8
# Aluno: Gabriel Max Vieira Matos - CC (UFCG)
# Atividade: Uri Table

graph = { "a" : ["c"],
               "b" : ["c", "e"],
               "c" : ["a", "b", "d", "e"],
               "d" : ["c","d"],
               "e" : ["c", "b"],
               "f" : []
       }

def max_degree(g):
	seq = []
	for vertex in g:
		seq.append(degree(vertex,g))
	seq.sort(reverse=True)
	return seq[0]

def min_degree(g):
	seq = []
	for vertex in g:
		seq.append(degree(vertex,g))
	seq.sort(reverse=False)
	return seq[0]

print max_degree(graph)
print min_degree(graph)
