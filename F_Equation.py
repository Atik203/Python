x, y = map(int, input().split())
S = 0
for i in range(0, (y+1), 2):
    if i == 0:
        S += x**i - 1
    else:
        S += x**i
print(S)