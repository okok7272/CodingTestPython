#분해합
N = int(input())
#입력
result = 0
#최대값을 넣어놓는 곳
for i in range(1, N+1):
    all = list(map(int, str(i)))
#i를 먼저 string타입으로 바꾸어 하나씩 읽을 수 있게 만듬
#그리고 나서 map을 이용하여 순차적으로 int타입으로 바꾸어 list에 입력
    result = i + sum(all)
    if result == N:
# 분해합이 N인 경우 정지
        print(i)
        break

    if i == N:
#다돌렸으나 결과 값이 없는 경우 stop
        print(0)
