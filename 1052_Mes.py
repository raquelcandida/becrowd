# solução 1
#mes = ['january','february','march','april','may','june','july','august','september','october','november','december']
#val = int(input())
#if (val > 0 and val <= 12):
#    val -= 1
#    valor = (mes[val])
#    valor1 = valor[0].upper()
#    print(f'{valor.replace(valor[0],valor1)}',end='')
#else:
#    print('valor invalido')

# solução 2 - aceita pelo beecrowd
mes = ['january','february','march','april','may','june','july','august','september','october','november','december']

val = int(input())

valor = mes[val-1].capitalize()

print(f'{valor}')

