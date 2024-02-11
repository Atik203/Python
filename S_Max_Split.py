s = input()
count_R = count_L = 0
balanced = []
for c in s:
    if c == 'R':
        count_R += 1
    else:
        count_L += 1
    if count_R == count_L:
        balanced.append(s[:count_R+count_L])
        s = s[count_R+count_L:]
        count_R = count_L = 0
        
print(len(balanced))
for i in balanced:
    print(i)
