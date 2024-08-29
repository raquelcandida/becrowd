l1 = []
l2 = []
l = []
cont = 0
s = 0
n, g = input().split(' ')

for i in range (int(n)):
    m = input().split(' ')
    l1.append(m[cont].upper())
    l2.append(int(m[cont+1]))
    cont = 0

x = int(input())
r = input().split(' ')

for i in range (x):
    l.append(r[i].upper())

for i in range (len(l)):
    for j in range (len(l1)):
        if l[i] == l1[j]:
            s = s + l2[j]
print(s)
if int(g) > s:
    print('My precioooous')
else:
    print('You shall pass!')


print(l2)
print(l1)
print(l)
print(f'g = {g}')

#8 10
#D 5
#B 5
#V 5
#A -10
#X -2
#S -4
#J 5
#R 5
#5
#D A B V R

