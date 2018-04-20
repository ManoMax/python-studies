# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Atividade: Sort Simples / CC (UFCG)

p = raw_input().split()
ordem = []
for i in range(len(p)):
	ordem.append(p[i])

troca = True
while troca:
	troca = False
	for i in range(len(p)-1, 0, -1):
		for j in range(i-1, -1, -1):
			if int(p[j]) >= int(p[i]):
				p[i], p[j] = p[j], p[i]
				troca = True
			else: break

for i in range(len(p)):
	print p[i]
print
for i in range(len(ordem)):
	print ordem[i]
