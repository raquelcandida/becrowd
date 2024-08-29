n = int(input())
a, b = input().split(" ")

if (2<= n <=100) and (1<= int(a)<=100) and (1<= int(b) <=100):
    if (int(a)+int(b)) > n:
        print(f'Deixa para amanha!',end="\n")
    else:
        print(f'Farei hoje!',end="\n")

#código abaixo aceito pelo beecrowd
n = int(input())
a, b = input().split(" ")

if (int(a)+int(b)) > n:
    print('Deixa para amanha!',end="\n")
else:
    print('Farei hoje!',end="\n")