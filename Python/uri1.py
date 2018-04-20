# coding: utf-8
# Aluno: Gabriel Max Vieira Matos
# Atividade: Tempo de Jogo com Minutos / CC (UFCG)

p = raw_input().split()
a = int(p[0])
b = int(p[1])
c = int(p[2])
d = int(p[3])

if a < c:
	hora = c - a
	if b < d:
		minu = d - b
	elif b > d:
		minu = 60 + d - b
		hora -= 1
	else:
		minu = 0
elif a > c:
	hora = 24 - a + c
	if b < d:
		minu = d - b
	elif b > d:
		minu = 60 + d - b
	else:
		minu = 0
else:
	hora = 24
	if b < d:
		hora = 0
		minu = d - b
	elif b > d:
		minu = 60 + d - b
		hora -= 1
	else:
		minu = 0

if minu == 60:
	minu = 0
	hora += 1
	
print 'O JOGO DUROU %d HORA(S) E %d MINUTO(S)' % (hora, minu)
