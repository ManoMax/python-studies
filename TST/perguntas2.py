# coding: utf-8
# Quiz: História da Computação!
# Grupo: Gabriel Matos
#        Mateus Rangel
#        Lukas Nascimento

import os

Equipe = raw_input("Digite o Nome da Equipe: ")
pontuacao = 0

print "\n Olá, seja Bem-Vindo ao Quiz: História da Computação!"
menu = int(raw_input("\n•Começar, digite 1.\n•Tutorial, digite 2.\n-Digite aqui: "))

while menu != 3:
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if menu == 2:
		print "Tutorial:\n"
		print "O jogo baseia-se em um Sistema de 10 Perguntas, no qual cada Alternativa correta equivalem a 10 pontos.\n"
		print "O jogador deverá dominar os conceitos da História da Computação.\nE a partir disso indicar a resposta correta.\n"
		print "Para isso, digite dentre as Alternativas 'a, b, c, d ou e' e siga adiante, até concluir as 10 perguntas."
		menu = int(raw_input("\nComeçar o Jogo, digite 1.\nVoltar ao menu, digite 3."))
		
	os.system('cls' if os.name == 'nt' else 'clear')
	
	if menu == 1:
		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 1.\n"
		print "1. Qual a primeira forma de cálculo desenvolvida?\n"
		print "a)Bastões de Napier;"
		print "b)Régua de Cálculos;"
		print "c)Abáco;"
		print "d)Código Morse;"
		print "e)Cartões de Jacquard."
		resposta1 = raw_input("\n-Resposta: ")
		if resposta1 == "c":
			pontuacao += 10
		
		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 2.\n"
		print "Quais os principais problemas enfrentados no sistema de Válvulas nos Computadores de 1950?\n"
		print "a) Grande, esquenta muito e consome muita energia;"
		print "b) Grande, dificil manutenção e pouco duráveis;"
		print "c) Grande, dificil manutenção e pouco viáveis;"
		print "d) Grande, pouco duráveis e pouco viáveis;"
		print "e) Esquenta muito, pouco duráveis e pouco viáveis."
		resposta2 = raw_input("\n-Resposta: ")
		if resposta2 == "a":
			pontuacao += 10

		os.system('cls' if os.name == 'nt' else 'clear')
			
		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 3.\n"
		print "Primeiro instrumento moderno de calcular?\n"
		print "a) Ábaco;"
		print "b) Máquina de Pascal;"
		print "c) Bastões de Napier;"
		print "d) Máquina Analítica;"
		print "e) Régua de Cálculos: o primeiro computador analógico."
		resposta3 = raw_input("\n-Resposta: ")
		if resposta3 == "b":
			pontuacao += 10
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 4.\n"
		print "As válvulas substituíram os relés e com isso veio a criação da:\n"
		print "a) Primeira Geração de Computadores;"
		print "b) Segunda Geração de Computadores;"
		print "c) Terceira Geração de Computadores;"
		print "d) Quarta Geração de Computadores;"
		print "e) Quinta Geração de Computadores."
		resposta4 = raw_input("\n-Resposta: ")
		if resposta4 == "a":
			pontuacao += 10
			
		os.system('cls' if os.name == 'nt' else 'clear')
			
		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 5.\n"
		print "\nA Evolução dos Computadores se baseia em quais pontos principais?\n"
		print "a) Memória e facilidade de uso;"
		print "b) Processamento e facilidade de uso;"
		print "c) Interatividade e rapidez;"
		print "d) Processamento de Armazenamento;"
		print "e) Processador e memória RAM."
		resposta5 = raw_input("\n-Resposta: ")
		if resposta5 == "d":
			pontuacao += 10
			
		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 6.\n"
		print "\nAs siglas 'QWERTY' ou 'AZERTY' e 'DVORAK' são referente a que?\n"
		print "a) Marcas de Memória RAM;"
		print "b) Cheats do GTA;"
		print "c) Modelos Padrão de Teclado;"
		print "d) Senhas Padrão do Linux;"
		print "e) Idiomas do SO."
		resposta6 = raw_input("\n-Resposta: ")
		if resposta6 == "c":
			pontuacao += 10

		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 7.\n"
		print "\nSistema Operacional mais importante do mundo, visto que trouxe um código livre e aberto. O principal destaque desse Software é que ele somente evoluiu sem necessidade de uma bela inferface gráfica e outros adicionais:\n"
		print "a) Windows XP;"
		print "b) Linux;"
		print "c) MAC OS X;"
		print "d) Windows 98;"
		print "e) Ubuntu."
		resposta7 = raw_input("\n-Resposta: ")
		if resposta7 == "b":
			pontuacao += 10

		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 8.\n"
		print "\nNa memória principal do computador:\n"
		print "a) Estão presentes as partes dos programas e dos dados que estão sendo processados naquele momento;"
		print "b) Estão presentes todos os programas e dados que podem ser processados pelo computador;"
		print "c) Estão presentes todos os comandos que compõem uma linguagem de programação;"
		print "d) Estão armazenadas as instruções de um único programa e está em execução naquele momento;"
		print "e) Estão armazenadas arquivos pessoais, como fotos de família, viagens, jogos e músicas."
		resposta8 = raw_input("\n-Resposta: ")
		if resposta8 == "a":
			pontuacao += 10

		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 9.\n"
		print "\nO que significa o termo WWW\n"
		print "a) West Wild World;"
		print "b) War With Warriors;"
		print "c) Where We Wait;"
		print "d) World Wild Web;"
		print "e) World Wide Web."
		resposta9 = raw_input("\n-Resposta: ")
		if resposta9 == "e":
			pontuacao += 10

		os.system('cls' if os.name == 'nt' else 'clear')

		print "Pontuação da Equipe(%s): %d/100" % (Equipe, pontuacao)
		print "\n Pergunta 10.\n"
		print "\nO número decimal 191 é representado, nos sistemas binário e hexadecimal como:\n"
		print "a) 10111111 e BF;"
		print "b) 10111111 e FB;"
		print "c) 10111001 e BD;"
		print "d) 10111001 e DE;"
		print "e) 10111101 e DE."
		resposta9 = raw_input("\n-Resposta: ")
		if resposta9 == "a":
			pontuacao += 10
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print "\n Olá, seja Bem-Vindo ao Quiz: História da Computação!"
		menu = int(raw_input("\n•Começar, digite 1.\n•Tutorial, digite 2.\n-Digite aqui: "))

print "A pontuação da sua Equipe(%s) foi de: %d/100" % (Equipe, pontuacao)
