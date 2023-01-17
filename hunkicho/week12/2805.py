# https://www.acmicpc.net/problem/2805

import sys

def binary_search(tree: list, height: int) -> None:
    pl = 0
    pr = max(tree)
    print_list = []
    

    while True:
        pc = (pl + pr) // 2                # 절단기 높이 설정
        cut_tree = 0                       # 자른 뒤 남은 나무들의 높이의 합

        for i in tree:
            if i > pc:                     # 나무가 절단기보다 높을 때만 나무를 잘라 가져갈 수 있다.
                cut_tree += i - pc

        if cut_tree >= height:             # 자른 나무들의 높이가 목표치 이상이면 리스트에 담아두기
            print_list.append(pc)
            pl = pc + 1                    # 목표치 보다 크면 높은 위치에서 잘라야 하기 때문에 + 1
        else:
            pr = pc - 1                    # 목표치 보다 작으면 낮은 위치에서 잘라야 하기 때문에 -1
        
        if pl > pr:
            break
        
    print(max(print_list))

if __name__ == "__main__":
    # 나무의 수 n
    # 가져가려는 나무의 길이 m
    # 나무들의 높이 리스트 tree
    n, m = map(int, sys.stdin.readline().split())
    tree = list(map(int, sys.stdin.readline().split()))
    tree.sort()

    binary_search(tree, m)