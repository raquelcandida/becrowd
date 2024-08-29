
a, b, c = input().split(" ")
maiorab = int(((int(a)+int(b)+abs(int(a)-int(b)))/2))
maiorn = int((maiorab+int(c)+abs(maiorab-int(c)))/2)
print(f'{maiorn} eh o maior')

