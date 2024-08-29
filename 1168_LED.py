n =int(input())

for i in range(0,n):
    val = str(input())
    cont = 0
    for j in range(0,len(val)):
        if val[j] == '0':
            cont = cont + 6
        elif val[j] == '1':
            cont = cont + 2
        elif val[j] == '2':
            cont = cont + 5
        elif val[j] == '3':
            cont = cont + 5
        elif val[j] == '4':
            cont = cont + 4
        elif val[j] == '5':
            cont = cont + 5
        elif val[j] == '6':
            cont = cont + 6
        elif val[j] == '7':
            cont = cont + 3
        elif val[j] == '8':
            cont = cont + 7
        elif val[j] == '9':
            cont = cont + 6

    print(f'{cont} leds')