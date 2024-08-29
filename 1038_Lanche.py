cod, qtd = input().split(" ")
total = 0.00
if (float(cod)) == 1:
    total = int(qtd) * 4.00
elif (float(cod)) == 2:
    total = int(qtd) * 4.50
elif (float(cod)) == 3:
    total = int(qtd) * 5.00
elif (float(cod)) == 4:
    total = int(qtd) * 2.00
elif (float(cod)) == 5:
    total = int(qtd) * 1.50
print(f'Total: R$ {total:.2f}')
