
T = input()
T = int(T)
numT = T
i = 0

while True:
    a = numT // 10
    b = numT % 10
    c = (a+b) % 10
    numT = (b * 10) + c

    i += 1
    if (numT == T):
        break
print(i)
