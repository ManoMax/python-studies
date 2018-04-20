# coding: utf-8
# Aluno: Gabriel Matos
# Matrícula: 117110060
# Atividade: Exercício Complementar 1

NDecimal = int(raw_input("Digite um Nº em Decimal: "))
NBinario = bin(NDecimal)
NOctal = oct(NDecimal)
NHexa = hex(NDecimal)

print "O Nº %d em Decimal: %d" % (NDecimal, NDecimal)
print "O Nº %d em Binário é: %s" % (NDecimal, NBinario[2:])
print "O Nº %d em Octal é: %s" % (NDecimal, NOctal[1:])
print "O Nº %d em HexaDecimal é: %s" % (NDecimal, NHexa[2:])
