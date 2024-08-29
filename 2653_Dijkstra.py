from sys import stdin

lista = []

val_ini : str

for val_ini in stdin:
    if not val_ini in lista:
        lista.append(val_ini)

print(len(lista))
