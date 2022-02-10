
T = input()
numT = int(T)

for i in range(0,numT):
    a,b = input().split()
    #split()는 공백 기준으로 나누어서 입력된다.
    a = int(a)
    b = int(b)
    # input()은 문자타입이기에 int()로 정수자료형으로 바꾼다.
    print(a+b)


