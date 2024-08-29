l = ['tesoura', 'papel','pedra','lagarto','spock','tesoura','lagarto','papel','spock','pedra','tesoura']
result = ''

n = int(input())

for _ in range(n):
    rajesh, sheldon = input().split(' ')

    if (rajesh == sheldon):
        result='empate'
    else:
        for i in range(len(l)-1):
            if (l[i] == rajesh and l[i+1] == sheldon):
                result ='rajesh'
                break
            elif (l[i]== sheldon and l[i+1]== rajesh):
                result='sheldon'
                break
    print(result)