n = []
for i in range(6):
    n.append(float(input()))
qtd = 0
for i in range(len(n)):
    if n[i] > 0:
        qtd = qtd + 1
print(f'{qtd} valores positivos')