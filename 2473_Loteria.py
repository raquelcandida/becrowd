#l1 = [34,55,77,12,23,99]
#l2 = [5,3,77,55,42,34]

# 22 41 9 71 88 4
# 41 9 88 71 4 22

# 25 51 53 17 19 87
# 23 33 1 2 81 92

l1 = []
l2 = []

cont = 0
n = input().split(' ')
m = input().split(' ')

for i in range(len(n)):
    l1.append(int(n[i]))

for i in range(len(m)):
    l2.append(int(m[i]))

for i in range (len(l1)):
    for j in range (len(l2)):
        if l1[i] == l2[j]:
            cont += 1

if cont == 3:
    print('terno')
elif cont == 4:
    print('quadra')
elif cont == 5:
    print('quina')
elif cont == 6:
    print('sena')
else:
    print('azar')