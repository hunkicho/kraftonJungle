# https://www.acmicpc.net/problem/9012

import sys

number = int(sys.stdin.readline())

for i in range(number):
    st = []
    check = list(sys.stdin.readline().rstrip())
    for j in check:
        if j == '(':
            st.append(j)
        elif j == ")":
            if len(st) > 0:
                st.pop()
            else:
                print("NO")
                break
    else:  # for ~ else 구문으로 for문에서 break 안걸리고 왔으면 실행하는 부분
        if len(st) == 0:
            print("YES")
        else:
            print("NO")