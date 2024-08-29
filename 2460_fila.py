n = int(input())
ent = input().split(' ')

m = int(input())
sai = input().split(' ')

for i in range (m):
    if sai[i] in ent:
        ent.remove(sai[i])

for i in range (len(ent)):
    print(ent[i], end = '' if i==len(ent)-1 else ' ')