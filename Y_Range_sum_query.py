N, Q = map(int, input().split())
A = list(map(int, input().split()))
prefix_sums = [0] * (N + 1)
for i in range(N):
    prefix_sums[i+1] = prefix_sums[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(prefix_sums[R] - prefix_sums[L-1])