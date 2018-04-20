import math

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

Delta = b**2 - (4 * a * c)
x1 = (-(b) + math.sqrt(abs(Delta))) / (2 * a)
x2 = (-(b) - math.sqrt(abs(Delta))) / (2 * a)

if Delta < 0:
	print "sem raizes reais"
elif x1 != x2:
	print "x1 = %.2f" % x1
	print "x2 = %.2f" % x2
else:
	X = x1
	print "x = %.2f" % X
