# https://www.acmicpc.net/problem/2798

# n: 카드의 갯수
# m: 합
# 조건: m을 넘지 않으면서 m에 가장 가까운 카드 3장의 합을 구한다

# 조합 -> combinations(반복 가능한 객체, r)
# 순열 -> permutations(반복 가능한 객체, r)
# 중복 조합 -> combinations_with_replacement(반복 가능한 객체, r)
# 중복 순열 -> product(반복 가능한 객체, repeat)

import sys
from itertools import combinations

if __name__ == "__main__":
    n , m = map(int, sys.stdin.readline().split())         # 카드의 갯수, 합
    number = list(map(int, sys.stdin.readline().split()))  # 카드들
    result = 0

    for i in combinations(number, 3):                      # 조합 구하기
        if result < sum(i) <= m:                           # 합이 조건에 부합하면
            result = sum(i)
    print(result)