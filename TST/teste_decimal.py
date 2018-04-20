num = raw_input()

resultado = 0
total = 0
aux = 0

for algarismo in range(len(num)-1,-1,-1):
    resultado = int(num[aux]) * (8 ** algarismo)
    print "%s * 8^%d = %d" % (num[aux], algarismo, resultado)
    total += resultado
    aux += 1

print "%s(8) = %d(10)" % (num, total)
