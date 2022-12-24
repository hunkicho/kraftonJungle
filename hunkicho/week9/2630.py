# https://www.acmicpc.net/problem/2630

import sys

def paper_count(x: int, y: int ,n: int) -> None:
    global p1
    global p0

    # 비교값 설정
    cmp = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 같은 수가 아니면
            if p[i][j] != cmp:
                # 4등분 하여 재귀
                paper_count(x, y, n // 2)
                paper_count(x, y + (n // 2), n // 2)
                paper_count(x + (n // 2), y, n // 2)
                paper_count(x + (n // 2), y + (n // 2), n // 2)
                return


    if cmp == 1:
        p1 += 1
    else:
        p0 += 1


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    p1 = 0
    p0 = 0  

    paper_count(0, 0, n)

    print(p0)
    print(p1)