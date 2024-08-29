l = []
x = int(input())
val = input().split(" ")
menor = int(val[0])
posicao = 0

for i in range(0,x):
    l.append(int(val[i]))
    if l[i] < menor:
        menor = l[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')