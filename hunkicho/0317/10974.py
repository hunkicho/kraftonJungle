import sys
from itertools import permutations

n = int(sys.stdin.readline())
num_list = []
for i in range(1, n + 1):
    num_list.append(i)

for i in permutations(num_list, n):
    print(*i)


# n = int(input())
# temp = []

# def dfs():
#     if len(temp) == n:
#         print(*temp)
#         return
#     for i in range(1, n + 1):
#         if i not in temp:
#             temp.append(i)
#             dfs()
#             temp.pop()

# dfs()