#coding: utf-8
dia = raw_input("Dia da semana? ")
orcamento = float(raw_input("Orcamento? R$ "))
adultos = int(raw_input("Numero de adultos? "))
criancas = int(raw_input("Numero de criancas? "))
pizza = float(raw_input("Preco da pizza? R$ "))
refrigerante = float(raw_input("Preco do refrigerante? R$ "))
estacionamento = float(raw_input("Preco do estacionamento? R$ "))
cinema = float(raw_input("Preco do ingresso do cinema? R$ "))

gastos_alimentacao = pizza + refrigerante
gastos_cinema = (cinema + 2) * adultos + (cinema / 2 + 2) * criancas
gastos_total = gastos_alimentacao + gastos_cinema + estacionamento
individual = gastos_total / (adultos + criancas)
saldo = orcamento - gastos_total

print "========== Despesas de " + str(dia) + " =========="
print "Despesas com alimentacao: R$ " + str(gastos_alimentacao)
print "Despesas com cimena: R$ " + str(gastos_cinema)
print "Despesas por pessoa: R$ " + str(individual)
print "Saldo disponivel: " + str(saldo)
