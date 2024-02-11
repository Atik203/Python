t = input()
for i in range(int(t)):
    x,y = input().split()
    start = min(int(x),int(y))
    end = max(int(x),int(y))
    sum = 0
    for i in range(start+1,end):
        if(i%2==1):
            sum += i
    print(sum)