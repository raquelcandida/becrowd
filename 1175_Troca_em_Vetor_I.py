#l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l=[]

for i in range(0,5):
    l.append(int(input()))

for i in range(0,len(l)):
    if i < 10:
        x=l[i]
        l[i]=l[len(l)-(i+1)]
        l[len(l)-(i+1)]=x

for i in range(0,len(l)):
    print(f'N[{i}] = {l[i]}')