#coding: utf-8

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
peso1 = float(raw_input()) / 100
peso2 = float(raw_input()) / 100
peso3 = 1 - (peso1 + peso2)
media = nota1 * peso1 + nota2 * peso2 + nota3 * peso3
print "Média Final: %.1f" % media
