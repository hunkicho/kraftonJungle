# https://www.acmicpc.net/problem/2805

import sys
count, length = list(map(int, sys.stdin.readline().split()))
tree = list(map(int, sys.stdin.readline().split()))

tree.sort(reverse=True)

for i in range(len(tree)):
    sum += tree[i] - tree[i+1]
    if sum >= length:
        if sum == length:
            print(tree[i+1])
        else:
            print(tree[i+1] + (sum - length))
        break
    
    