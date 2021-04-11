num = int(input())
cont = 0
 
array_x = []
array_y = []
used = [0] * num


for i in range(num):
	ax, ay = [int(j) for j in input().split()]
	array_x.append(ax)
	array_y.append(ay)
def aux(elem):
  used[elem] = 1
  for i in range(num):
    if not used[i] and (array_x[i] == array_x[elem] or array_y[i] == array_y[elem]):
      aux(i)
for i in range(num):
	if not used[i]:
		aux(i)
		cont = cont + 1
 
print(cont-1)