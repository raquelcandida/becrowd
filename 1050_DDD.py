n = int(input())
ddd = [61,71,11,21,32,19,27,31]
destination = ['Brasilia','Salvador','Sao Paulo','Rio de Janeiro','Juiz de Fora','Campinas','Vitoria','Belo Horizonte']
x = -1
for i in range(len(ddd)):
    if n == ddd[i]:
        x = i
if x != -1 :
    print(f'{destination[x]}')
else:
    print('DDD nao cadastrado')