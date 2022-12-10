# https://www.acmicpc.net/problem/2504

import sys

st = []
input = sys.stdin.readline()
status = 1
print_num = 0

for i in input:

    if i == '(' or i == '[':
        st.append(i)
    elif i == ')':
        if len(st) < 1:
                status = 0
                break
        while st[-1] != '(':
            st.pop()
        st.pop()
        print_num += 2
    elif i == ']':
        while st[-1] != '[':
            if len(st) < 1:
                status = 0
                break
            st.pop()
        st.pop()
        print_num += 3
    
    if status == 0:
        print(0)
        break



if status == 1:
    print(print_num)