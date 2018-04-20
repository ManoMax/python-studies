#coding: utf-8
import math

velocidade = float(raw_input())
raio = float(raw_input()) / 2
tempo = float(raw_input())
area = math.pi * raio**2
agua = velocidade * raio * tempo

print "Quantidade de água = %f litros." % agua
