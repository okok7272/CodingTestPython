# #2750식으로 풀면 에러가 발생
# #버블sort사용
# N = int(input())
#
# M = []
#
# for i in range(N):
#     M.append(int(input()))
#
# for i in range(len(M)):
#     for j in range(len(M)):
#         if M[i] < M[j]:
#             M[i], M[j] = M[j], M[i]
#
# for i in M :
#     print(i)
# #시간초과

#merge sort 사용

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) //2
    left = merge_sort(array[:mid])
    #중간점 중심으로 왼쪽
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k +=1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr = merge_sort(arr)

for i in arr:
    print(i)

#sorted 함수 이용
n = int(input())
num = []

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)