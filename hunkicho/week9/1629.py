# https://www.acmicpc.net/problem/1629
# 못 풀었다.

# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
# 분할정복으로 재귀
# 2^10 = 2^5 * 2^5
# 2^11 = 2^5 * 2^5 * 2

import sys

def half(n1: int, n2: int, n3: int) -> int:
    # 1제곱은 밑수 그대로
    if n2 == 1:
        return n1 % n3

    # 재귀로 절반 구하기
    temp = half(n1, n2 // 2, n3)

    if n2 % 2 == 0:                       # 지수가 짝수여서 절반으로 나눌 수 있는 경우
        return temp * temp % n3
    else:                                 # 지수가 홀수여서 절반으로 나눌 수 없는 경우 
        return temp * temp * n1 % n3
    

a, b, c = map(int, sys.stdin.readline().split())

print(half(a,b,c))