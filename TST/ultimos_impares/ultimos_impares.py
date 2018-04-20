n = int(raw_input())
limite = int(raw_input())
sequencia = []
soma = 0

for i in range(n):
	sequencia.append(int(raw_input()))

for num in sequencia:
	soma += num
	if soma <= limite:
		if num % 2 == 1:
			ultimo_impar = num
	elif soma > limite:
		if num % 2 == 1:
			soma = ultimo_impar + num
print soma
