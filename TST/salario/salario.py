#coding: utf-8
bruto = float(raw_input())
horas = float(raw_input())
ganho = float(bruto / horas)
IR = float(bruto * 0.11)
INSS = float(bruto * 0.08)
Sindicato = float(bruto * 0.05)
Salario = float(bruto - (IR + INSS + Sindicato))
Hora = Salario / horas
print "Salário Bruto = " + str(bruto)
print "Hora Bruta = " + str(ganho)
print "Desconto IR = " + str(IR)
print "Desconto INSS = " + str(INSS)
print "Desconto Sindicato = " + str(Sindicato)
print "Salário Líquido = " + str(Salario)
print "Hora Líquida = " + str(Hora)tst
