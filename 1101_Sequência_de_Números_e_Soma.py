val = ''
sum = 0
m, n =input().split(' ')

while (int(m) > 0) and (int(n) > 0):
    if int(m) > int(n):
       y = int(m)
       m = int(n)
       n = int(y)

    for i in range(int(m),int(n)+1):
        val = val + str(i) + ' '
        sum = sum + i

    print(f'{val}Sum={sum}')
    sum = 0
    val = ''
    m, n=input().split(' ')