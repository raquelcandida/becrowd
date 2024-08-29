l = []
cont = 0
t =int(input())
for i in range(0,1000):
    l.append(cont)
    if cont == t-1:
        cont = 0
    else:
        cont += 1
    print(f'N[{i}] = {l[i]}')