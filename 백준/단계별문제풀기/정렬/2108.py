import sys
from collections import Counter

numbers = []
#N = int(input())
#시간초과로 sys 불러옴
N = int(sys.stdin.readline())
for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)

numbers.sort()

cnt = Counter(numbers).most_common(2)

print(round(sum(numbers)/len(numbers)))
#산술평균
print(numbers[len(numbers)//2])
#중앙값
if len(numbers) >1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
#최빈값
print(max(numbers)-min(numbers))
#