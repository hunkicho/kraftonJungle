# https://www.acmicpc.net/problem/1992
# 2주차 테스트 문제


# https://seraup.dev/5
# 첫번째 예시
import sys

x = int(input())
mat = [input() for _ in range(x)]

def quad(x1, y1, x2, y2, n):
    if n == 1:
        return mat[y1][x1]

    a = n // 2

    # 4등분으로 분할
    r1 = quad(x1, y1, x1+a, y1+a, a)
    r2 = quad(x1+a, y1, x1+n, y1+a, a)
    r3 = quad(x1, y1+a, x1+a, y1+n, a)
    r4 = quad(x1+a, y1+a, x1+n, y1+n, a)

    # 모두 같은 값일 경우 하나만 출력
    if r1 == r2 == r3 == r4 and len(r1) == 1:
        return r1

    return "(" + r1 + r2 + r3 + r4 + ")"

print(quad(0,0,x,x,x))