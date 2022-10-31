# https://www.acmicpc.net/problem/2628

import sys

length = list(map(int, sys.stdin.readline().split()))
cut_count = int(sys.stdin.readline())

for i in (cut_count):
    cut1 = list(map(int, sys.stdin.readline().split()))
    if cut1[0] == 0:
        if cut1[1] > length[0] - cut1[1]:
            
cut2 = list(map(int, sys.stdin.readline().split()))
cut3 = list(map(int, sys.stdin.readline().split()))

