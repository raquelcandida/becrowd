notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

val = float(input())
cont = 0

print('NOTAS:')
for i in range (len(notas)):
    cont = int(val / notas[i])
    print(f'{cont} nota(s) de R$ {notas[i]:.2f}')
    val = val % notas[i]

print('MOEDAS:')
for i in range (len(moedas)):
    cont = int(round(val,2) / moedas[i])
    print(f'{cont} moeda(s) de R$ {moedas[i]:.2f}')
    val = round(val,2) % moedas[i]