str1 = input()
str2 = input()

def compare(s):
    if (len(s) % 2 == 1):
        return s
        
    half = int(len(s) / 2)
    s1 = compare(s[0:half])
    s2 = compare(s[half:len(s)])

    if (s1 < s2):
        return s1 + s2
    else:
        return s2 + s1

if (compare(str1) == compare(str2)):
    print('YES')
else:
    print('NO')
