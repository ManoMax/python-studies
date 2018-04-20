# coding: utf-8
# Aluno: Samuel Lucas V. Matos
# Matricula: Nenhuma
# Questão: Semi César - CC (UFCG)

def cesar(msg, d):
	result = ''
	if len(msg) == 0:
		result = ''
		
	else:
		for i in range(len(msg)):
			letter = msg[i]
			
			for i in range(len(letter)):
				if ord(letter[i]) >= 97 and ord(letter[i]) <= 122:
					
					if d >= 0:
						if ord(letter[i]) + d <= 122:
							result += chr(ord(letter[i])+d)
						elif ord(letter[i]) + d > 122:
							num = int(ord(letter[i]) + d) - 122
							result += chr(96 + num)
							
					elif d < 0:
						if ord(letter[i]) + d < 97:
							num = int(ord(letter[i]) + 26) + d
							result += chr(num)
						else:
							result += chr(ord(letter[i]) + d)
				
				else:
					result += letter[i]
	return result

assert cesar('exemplo', 4) == 'ibiqtps'
assert cesar('Exemplo 2!', 4) == 'Ebiqtps 2!'
