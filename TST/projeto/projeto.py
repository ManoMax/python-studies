# coding: utf-8
# Aluno: Gabriel Matos
# Matricula: 117110060
# Atividade: Seleção Projeto

CRE = float(raw_input())
meses = int(raw_input())
nota = float(raw_input())

if CRE >= 7.0 and meses >= 6:
	if nota <= 3.0:
		print "Candidato classificado."
	if nota > 3.0:
		print "Candidato aprovado."

if meses < 6:
	if CRE >= 7.0:
		print "Candidato eliminado. Experiência abaixo do limite."
	if CRE < 7.0:
		print "Candidato eliminado. CRE e experiência abaixo do limite."
		
if CRE < 7.0:
	if meses >= 6:
		print "Candidato eliminado. CRE abaixo do limite."
	if meses < 6:
		print "Candidato eliminado. CRE e experiência abaixo do limite."
		
