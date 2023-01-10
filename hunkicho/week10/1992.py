# https://www.acmicpc.net/problem/1992

import sys

def dfs(x: int, y: int, count: int):
    global str_print
    cmp = quad[x][y]
    
    for i in range(x, x + count):
        for j in range(y, y + count):
            if cmp != quad[i][j]:
                str_print += "("
                dfs(x, y, count // 2)
                dfs(x, y + (count // 2), count // 2)
                dfs(x + (count // 2), y, count // 2)
                dfs(x + (count // 2), y + (count // 2), count // 2)
                str_print += ")"
                return
    str_print += str(cmp)
    
                

if __name__ == "__main__":
    count = int(sys.stdin.readline())
    
    str_print = ""
    quad = []

    quad = [list(map(int, sys.stdin.readline().strip())) for _ in range(count)]
    
    dfs(0, 0, count)
    print(str_print)