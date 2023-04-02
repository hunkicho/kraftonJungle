# https://www.acmicpc.net/problem/2798

import sys

n, m = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

result = 0
max = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if card_list[i] + card_list[j] + card_list[k] > m:
                continue
            else:
                result = card_list[i] + card_list[j] + card_list[k]
                if max < result:
                    max = result
print(max)