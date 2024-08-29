n = int(input())
x = 0
y = 1
if 0 < n < 46:
    for i in range(0,n):
        if (i < 2):
            if i < n-1:
                print(i,end=" ")
            else:
                print(i)
        else:
            if i < n-1:
                print(x + y,end=" ")
            else:
                print(x + y)
            z = x
            x = y
            y = z + y
