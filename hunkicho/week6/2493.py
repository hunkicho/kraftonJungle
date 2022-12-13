# https://www.acmicpc.net/problem/2493

import sys

count = int(sys.stdin.readline().strip())

t_group = list(map(int, sys.stdin.readline().split()))
st = [[0, t_group[0]]]
print_list = ""

for i in range(1, count):
    if t_group[i] < st[len(st) - 1][1]:
        print_list += str(i + 1) + " "
        st.append([i, t_group[i]])
    else:
        st.pop()
        st.append([i, t_group[i]])

print(print_list)