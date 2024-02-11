# from collections import Counter
# we can alternatively count the frequency using Counter() 

n = int(input())
a = list(map(int, input().split()))

counts = {}
for num in a:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

count = 0
for num, freq in counts.items():
    if freq > num:
        count += freq - num
    elif freq < num:
        count += freq    
print(count)