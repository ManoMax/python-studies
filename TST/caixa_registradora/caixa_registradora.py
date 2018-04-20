# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Caixa Registradora - CC (UFCG)

def caixa_registradora(values, objective):
	add = 0
	commission = 0
	for i in range(len(values)):
		add += float(values[i])
		
		if values[i] < 1000:
			commission += values[i] * 0.05
		elif values[i] >= 1000 and values[i] < 5000:
			commission += values[i] * 0.1
		elif values[i] >= 5000:
			commission += values[i] * 0.15

		gain = add - commission
		if gain >= objective:
			situation = 'Lucro'
		else:
			situation = 'Prejuizo'
		
		result = [add, commission, situation]
	return result

assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
