n = int(input())
a,b = 0,1
for i in range(n):
    print(a,end=' ')
    temp = b
    b = a+b
    a = temp
        