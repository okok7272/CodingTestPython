
#2739 구구단
#input()으로 받으면 문자열이니 주의
number = input()
#주의할 점 range는 (a,b)범위이면 a이상 b미만이다.
for i in range(1,10):
    mul = i * int(number)
    print(number,'*',i,'=',mul)