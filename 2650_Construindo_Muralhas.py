n, w = input().split(' ')

for i in range (int(n)):
    m = input().split()
    alt = int(m[len(m)-1])
    nome = ""
    for j in range(len(m)-1):
        nome += m[j]
        if j < len(m)-2: nome += " "
    if alt > int(w): print(nome)
