#coding: utf-8

Preco = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
altura = float(raw_input("Digite a altura do tijolo (Em metros): "))
comprimento = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
Altura = float(raw_input("Digite a altura das paredes (Em metros): "))
Comprimento = float(raw_input("Digite o comprimento das paredes (Em metros): "))
TijolosA = Altura / altura
TijolosC = Comprimento / comprimento
Total = TijolosA * TijolosC
Orcamento = Total * Preco

print "O número total de tijolos é %.1f e o orçamento final é de R$ %.1f" % (Total, Orcamento)
