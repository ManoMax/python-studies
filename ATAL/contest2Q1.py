num1, num2 = map(int, input().split())
array=[]
array.append(num2)
while num2 > num1:
    if (num2 % 10 == 1):
        num2 = num2 // 10
    elif (num2 % 2 == 0):
        num2 = num2 // 2
    else:
        break
    array.append(num2)
if num2 == num1:
    array.reverse()
    print("YES")
    print(len(array))
    print(*array)
else:
    print("NO") 