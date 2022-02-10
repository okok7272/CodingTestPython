N = input()
N = int(N)#과목 수 입력 및 int형으로 정의
test_list = list(map(int, input().split()))
max_score = max(test_list)
new_list = []
for score in test_list:
    new_list.append(score/max_score * 100)
test_avg =sum(new_list)/N
print(test_avg)


