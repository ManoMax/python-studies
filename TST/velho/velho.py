nome1 = raw_input()
dia1 = int(raw_input())
mes1 = int(raw_input())
ano1 = int(raw_input())

nome2 = raw_input()
dia2 = int(raw_input())
mes2 = int(raw_input())
ano2 = int(raw_input())

if ano1 > ano2:
	print nome2
elif ano2 > ano1:
	print nome1
else:
	if mes1 > mes2:
		print nome2
	elif mes2 > mes1:
		print nome1
	else:
		if dia1 > dia2:
			print nome2
		elif dia2 > dia1:
			print nome1
		else:
			print "nenhuma"
