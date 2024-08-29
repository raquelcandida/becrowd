l = []
x =int(input())
for i in range(0,10):
    if i == 0:
        l.append(x)
    else:
        l.append(l[i-1]*2)
    print(f'N[{i}] = {l[i]}')