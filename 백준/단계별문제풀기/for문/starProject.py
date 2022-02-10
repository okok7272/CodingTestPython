#오른쪽 스타트 별찍기 기본

T = input()
T = int(T)

for i in range(T):
    for j in range(i+1):
        print('*', end="")
    print('')

#왼쪽으로 스타트

Q = input()
Q = int(Q)

for i in range(1,Q+1):
    for j in range(Q-i):
        print(' ', end="")
    for j in range(i):
        print('*', end="")
    print('')


#역으로 별찍기

R = input()
R = int(R)

for i in range(R,0,-1):
    for j in range(i):
        print('*', end="")
    print('')

#왼쪽 역으로 찍기

O = input()
O = int(O)
for i in range(O):
    for j in range(i):
        print(' ', end="")
    for j in range(O-i):
        print('*', end="")
    print('')

#피라미드