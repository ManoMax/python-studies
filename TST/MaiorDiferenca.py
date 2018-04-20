tamanho = int(raw_input())
sequencia = []
var = 0
num1 = 0
num2 = 0

for i in range(0, tamanho):
	sequencia.append(float(raw_input()))
	
for num in range(0, tamanho -1):
	if abs(sequencia[num] - sequencia[num+1]) > var:
		var = abs(sequencia[num] - sequencia[num+1])
		num1 = sequencia[num]
		num2 = sequencia[num+1]
		
print var
print "%.1f e %.1f" % (num1, num2)
