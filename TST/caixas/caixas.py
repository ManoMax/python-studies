#coding: utf-8
capacidade = float(raw_input("Capacidade de revestimento? "))

print "\n"
print "== Dados do vão a revestir =="
comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura? "))

CA = comprimento * altura
LA = largura * altura
chao = comprimento * largura
area = CA * 2 + LA * 2 + chao
caixas = area / capacidade

print "\n"
print "== Resultados =="
print "Área total a revestir: %.1f m2" % area
print "Número de caixas:", int(caixas)
