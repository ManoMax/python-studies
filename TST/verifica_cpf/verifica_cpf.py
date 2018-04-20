# coding: utf-8
# Aluno: Gabriel M. V. Matos
# Matricula: 117110060
# Questão: Dígitos de Verificação do CPF - CC (UFCG)

def calcula_digitos_verificacao(cpf):
	soma = 0
	cont = 1
	for i in range(len(cpf)-1, -1, -1):
		cont += 1
		mult = int(cpf[i]) * cont
		soma += mult
		if i == 0:
			result = (10 * soma) % 11
	if result != 10:
		cpf += str(result)
	else:
		result = 0
		cpf += '0'
		
	cont = 1
	soma = 0
	for j in range(len(cpf)-1, -1, -1):
		cont += 1
		mult = int(cpf[j]) * cont
		soma += mult
		if j == 0:
			result2 = (soma * 10) % 11
	
	final = str(result) + str(result2)
	return final
	
assert calcula_digitos_verificacao('153245875') == '40'
