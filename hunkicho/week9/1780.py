# https://www.acmicpc.net/problem/1780

import sys

def count_paper(x: int, y: int, n: int) -> None:
    global p_
    global p0
    global p1
    
    cmp = p[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if p[i][j] != cmp:
                count_paper(x, y, n // 3)
                count_paper(x, y + (n // 3), n // 3)
                count_paper(x, y + (n // 3) * 2, n // 3)
                count_paper(x + (n // 3), y, n // 3)
                count_paper(x + (n // 3), y + (n // 3), n // 3)
                count_paper(x + (n // 3), y + (n // 3) * 2, n // 3)
                count_paper(x + (n // 3) * 2, y, n // 3)
                count_paper(x + (n // 3) * 2, y + (n // 3), n // 3)
                count_paper(x + (n // 3) * 2, y + (n // 3) * 2, n // 3)
                return
    if cmp == -1:
        p_ += 1
    if cmp == 0:
        p0 += 1
    if cmp == 1:
        p1 += 1

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    p_ = 0
    p0 = 0
    p1 = 0
    
    count_paper(0, 0, n)
    
    print(p_)
    print(p0)
    print(p1)