# https://www.acmicpc.net/problem/17608

import sys

count = int(sys.stdin.readline())
st = []
hap  = 1

for i in range(count):
    st.append(int(sys.stdin.readline()))

check = st[-1]

for i in range(len(st) - 1, -1, -1):
    if st[i] > check:
        hap += 1
        check = st[i] # 이거 하는 이유는 맨 오른쪽 보다 더 큰거 나오면 그거 보다 작은 것도 안보이니까
print(hap)