l = []
x = float(input())
l.append(x)
for i in range(1,100):
    l.append(l[i-1]/2.0)

for i in range(len(l)):
    print(f'N[{i}] = {l[i]:.4f}')