# https://www.acmicpc.net/problem/12865

# n = 물건의 개수
# w = 물건의 무개
# v = 물건의 가치
# k = 최대 무게

# 

import sys

n, k = map(int, sys.stdin.readline().split())
things = []
maximun = 0

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    things.append([w,v])

things.sort(key=lambda x: x[0])

for i in things:
    for j in range(n):
        if i[]