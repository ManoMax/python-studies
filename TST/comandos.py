a = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
a[5] = -1
assert a[5] == -1
assert a == [0, 1, 4, 9, 16, -1, 36, 49, 64, 81]

print a

s = "casa"
assert list(s)
