x, s, y = input().split(" ")
a = x.replace("7","0")
b = y.replace("7","0")

if(0 < int(a) < 10000) and (0 < int(b) < 10000):
    if s.upper() == '+':
        result = str(int(a) + int(b))
    elif s.upper() == 'X':
        result = str(int(a) * int(b))

print(int(result.replace("7","0")))