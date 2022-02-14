N, K = map(int, input().split())
M = []

num = 0

for i in range(N):
    M.append(int(input()))
for i in range(N-1, -1, -1):
    if K == 0 :
        break
    if M[i] > K:
        continue
    num += K // M[i]
    K %= M[i]

print(num)
