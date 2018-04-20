atual = float(raw_input("Valor atual? "))
novo = float(raw_input("Novo valor? "))
porcentagem = (novo * 100 / atual)
reajuste = porcentagem - 100
print "Reajuste de %.1f%%" % reajuste
