#정렬
#정렬은 가장 중요한 파트로
# N = int(input())
# M = set()
# #중복되지 않으니 set
#
# for i in range(N):
#     M.add(int(input()))
# M = list(M)
# M.sort()
# for i in range(len(M)):
#     print(M[i])

N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

M = sorted(M)

for i in range(len(M)):
    print(M[i])
