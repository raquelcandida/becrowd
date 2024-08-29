# Solução que passou beecrowd
runas = dict()
soma = 0

n, g = input().split(' ')

for i in range (int(n)):
    m = input().split(' ')
    runas[m[0]] = int(m[1])

x = int(input())
r = input().split(' ')

for i in r:
    if i in runas:
        soma += runas[i]

print(f'{soma}')

if int(g) > soma:
    print('My precioooous')
else:
    print('You shall pass!')