t = int(input())
n = []
if (n >= 2 and n <=50):
    for i in range(10):
        if i != t-i:
            n[i]=i


for i in range(10):
    print(f'N[{i}] = {n[i]}')
