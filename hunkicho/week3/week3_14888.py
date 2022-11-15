# https://www.acmicpc.net/problem/14888


# 시간초과
# import sys
# from itertools import permutations

# count = int(sys.stdin.readline().strip())
# num = list(map(int, sys.stdin.readline().split()))
# oper = list(map(int, sys.stdin.readline().split()))
# op = []
# check = 0  # 0: '+', 1: '-', 2: '*', 3: '/' 
# hap = 0
# max_num = -1000000001   # 최대
# min_num = 1000000001    # 최소

# for i in oper:
#     if i != 0:
#         for _ in range(i):
#             op.append(check)
#     check += 1

# combi = list(permutations(op, len(op)))

# for j in combi:
#     hap = num[0]
#     for k in range(1,len(num)):
        
#         if j[k-1] == 0:
#             hap += num[k]
#         if j[k-1] == 1:
#             hap -= num[k]
#         if j[k-1] == 2:
#             hap *= num[k]
#         if j[k-1] == 3:
#             hap //= num[k] 

#     if hap > max_num:
#         max_num = hap
#     if hap < min_num:
#         min_num = hap

# print(min_num)
# print(max_num)


# https://data-flower.tistory.com/72

import sys

count = int(sys.stdin.readline().strip())           # 수의 갯수
num = list(map(int, sys.stdin.readline().split()))  # 수열 입력받기
add, sub, mul, div = map(int, sys.stdin.readline().split()) # 연산자 갯수 계산 

max_num = -1000000001   # 최대
min_num = 1000000001    # 최소

def dfs(i, arr):
    global add, sub, mul, div, max_num, min_num

    if i == count:
        max_num = max(max_num, arr)
        min_num = min(min_num, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, arr + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, arr * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, arr // num[i])
            div += 1

dfs(1,num[0])

print(min_num)
print(max_num)