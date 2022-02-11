#브루트 포스 블랙 잭
N, M = map(int, input().split())
#map 1. 자료타입 2.순차적 접근이 가능한 객체를 받음
arr = list(map(int, input().split()))
#list도 순차적 접근이 가능한 map으로 구현

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j]+ arr[k] > M:
                continue
#숫자가 초과하면 넘어감
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
#max 값의 계속 그 전에 조건을 충족하는 값과 비교하여 가장 높은 값을 result를 받음
print(result)