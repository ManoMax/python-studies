# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Tradutor Morse - CC (UFCG)

def tradutor_morse(lista):
	saida = ''
	for i in range(len(lista)):
		if lista[i] == '.-':
			saida += 'a'
		elif lista[i] == '-...':
			saida += 'b'
		elif lista[i] == '-.-.':
			saida += 'c'
		elif lista[i] == '-..':
			saida += 'd'
		elif lista[i] == '.':
			saida += 'e'
		elif lista[i] == '..-.':
			saida += 'f'
		elif lista[i] == '--.':
			saida += 'g'
		elif lista[i] == '....':
			saida += 'h'
		elif lista[i] == '..':
			saida += 'i'
		elif lista[i] == '.---':
			saida += 'j'
		elif lista[i] == '-.-':
			saida += 'k'
		elif lista[i] == '.-..':
			saida += 'l'
		elif lista[i] == '--':
			saida += 'm'
		elif lista[i] == '-.':
			saida += 'n'
		elif lista[i] == '---':
			saida += 'o'
		elif lista[i] == '.--.':
			saida += 'p'
		elif lista[i] == '--.-':
			saida += 'q'
		elif lista[i] == '.-.':
			saida += 'r'
		elif lista[i] == '...':
			saida += 's'
		elif lista[i] == '-':
			saida += 't'
		elif lista[i] == '..-':
			saida += 'u'
		elif lista[i] == '...-':
			saida += 'v'
		elif lista[i] == '.--':
			saida += 'w'
		elif lista[i] == '-..-':
			saida += 'x'
		elif lista[i] == '-.--':
			saida += 'y'
		elif lista[i] == '--..':
			saida += 'z'
	return saida
	
assert tradutor_morse(['.--.', '-.--', '-', '....', '---', '-.']) == 'python'
