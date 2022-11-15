# https://www.acmicpc.net/problem/11725

import sys

count = int(sys.stdin.readline().strip())
graph = [[] for _ in range(count + 1)]

for _ in range(count):
    start, end = map(int, sys.stdin.readline())

    graph[start].append(end)
    graph[end].append(start)

