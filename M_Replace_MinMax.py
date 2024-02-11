n = int(input())
a = list(map(int,input().split()))
mn = min(a)
mx = max(a)
min_index = a.index(mn)
max_index = a.index(mx)
a[min_index], a[max_index] = a[max_index], a[min_index]
print(*a)