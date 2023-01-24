# https://www.acmicpc.net/problem/2512

import sys

def binary_search(budget: list, limit: int) -> None:
    pl = 0
    pr = max(budget)
    print_num = 0

    while True:
        pc = (pl + pr) // 2             # 상한액
        hap = 0                         # 예산 배정액 합

        for i in budget:
            if i <= pc:                 # 예산 요청액이 상한액 이하이면 
                hap += i                # 예산 그대로 배정
            else:
                hap += pc               # 상한액 초과이면 상한액 배정
        
        if hap > limit:                 # 총 배정액 합이 총 예산 보다 크면
            pr = pc - 1                 # 검색 범위 절반으로 줄인다.
        else:
            if pc > print_num:          # 배정액의 합이 총 예산 이하일 때 최대값 설정
                print_num = pc
            pl = pc + 1                 # 검색 범위 절반으로 줄인다.

        if pl > pr:
            break
        
    print(print_num)


if __name__ == "__main__":
    count = int(sys.stdin.readline())                       # 지방의 수
    budget = list(map(int, sys.stdin.readline().split()))   # 지방의 예산 요청
    limit = int(sys.stdin.readline())                       # 총 예산
    binary_search(budget, limit)
