# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Karel o Robô - CC (UFCG)

Y = 0
X = 0
while True:
	input_ = raw_input().split()
	function = input_[0]
	move = input_[1]
	if move == '0':
		print "Fim de jogo"
		break
	if function == 'C':
		Y += int(move)
	elif function == 'B':
		Y -= int(move)
	elif function == 'D':
		X += int(move)
	elif function == 'E':
		X -= int(move)
				
	point = "(%.d, %d)" % (X, Y)
	Xp = X
	Yp = Xp + Xp
	portal = "(%.d, %.d)" % (Xp, Yp)
	
#	print point, portal
	if point == portal:
		print "Parabéns, conquista do portal", portal	
		break
	Yp = -Yp
	portal = "(%.d, %.d)" % (Xp, Yp)
	if point == portal:
		print "Parabéns, conquista do portal", portal
		break
