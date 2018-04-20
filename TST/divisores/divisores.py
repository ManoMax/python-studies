num = raw_input()
x = 0

for possibilidades in range(1, int(num)):
	x += 1
	if int(num) % possibilidades == 0:
		print x
