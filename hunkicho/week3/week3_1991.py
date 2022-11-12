# https://www.acmicpc.net/problem/1991

# https://daydreamx.tistory.com/entry/baekjoon1991

import sys

def preorder(node):         # 전위 순회
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):          # 중위 순회
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):        # 후위 순회
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')


N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = [left, right]


preorder('A')
print()

inorder('A')
print()

postorder('A')
print()