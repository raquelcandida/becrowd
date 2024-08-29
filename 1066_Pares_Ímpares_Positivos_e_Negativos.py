n = []
for i in range(5):
    n.append(float(input()))
npos = 0
nneg = 0
nimpar = 0
npar = 0
for i in range(len(n)):
    if n[i] > 0:
        npos += 1
    elif n[i] < 0:
        nneg += 1

    if (n[i] % 2 == 0):
        npar += 1
    else:
        nimpar += 1
print(f'{npar} valor(es) par(es)')
print(f'{nimpar} valor(es) impar(es)')
print(f'{npos} valor(es) positivo(s)')
print(f'{nneg} valor(es) negativo(s)')