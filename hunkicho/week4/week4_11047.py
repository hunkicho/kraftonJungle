# https://www.acmicpc.net/problem/11047

import sys

n, k = map(int, sys.stdin.readline().split())

coin = []
count = 0

for _ in range(n):
    input = int(sys.stdin.readline().strip())
    if input <= k:
        coin.append(input)

coin.sort(reverse=True)

for i in coin:
    if i <= k:
        count += k // i
        if k % i == 0:
            print(count)
            break
        else:
            k = k % i