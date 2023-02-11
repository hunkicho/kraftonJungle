# https://www.acmicpc.net/problem/10815

import sys

def bin_search(numbers: list ,key: int) -> int:
    pl = 0
    pr = len(numbers) - 1

    while True:
        pc = (pl + pr) // 2

        if numbers[pc] == i:
            return 1
        elif numbers[pc] > i:
            pr = pc - 1
        else:
            pl = pc + 1

        if pl > pr:
            return 0

if __name__ == "__main__":
    # search_list에서 get_list가 있는지 찾기
    get_count = int(sys.stdin.readline())
    get_list = list(map(int, sys.stdin.readline().split()))
    get_list.sort()

    search_count = int(sys.stdin.readline())
    search_list = list(map(int, sys.stdin.readline().split()))

    answer_list = []

    for i in search_list:
        answer_list.append(bin_search(get_list, i))
    print(*answer_list)


# 밑에는 시간 빠르게 나온 사람거 봤다.
# 파이썬 문법 잘 알아야 겠다
# import sys

# M = sys.stdin.readline()
# card = set(sys.stdin.readline().split())
# N = sys.stdin.readline()
# print("".join("1 " if i in card else "0 " for i in sys.stdin.readline().split()))