import sys
sys.setrecursionlimit(3000)
 
(num1, num2) = map(int, input().split())
array = []
used = []
result = 'No'
for i in range(num1):
    array.append(input())
    used.append([False]*num2)
 
def aux(index_i, index_J, previ, prevj, letter):
    global used
    global result
    used[index_i][index_J] = True
 
    for move in [(index_i+1,index_J),(index_i-1,index_J),(index_i,index_J+1),(index_i,index_J-1)]:
        if 0 <= move[0] < num1 and 0 <= move[1] < num2 and not used[move[0]][move[1]] and letter == array[move[0]][move[1]]:
            aux(move[0], move[1], index_i, index_J, letter)
        elif 0 <= move[0] < num1 and 0 <= move[1] < num2 and used[move[0]][move[1]] and letter == array[move[0]][move[1]] and (move[0] != previ or move[1] != prevj):
            result = 'Yes'
 
for index_i in range(num1):
    for index_J in range(num2):
        if not used[index_i][index_J]:
            aux(index_i, index_J, -1, -1, array[index_i][index_J])
 
print(result)