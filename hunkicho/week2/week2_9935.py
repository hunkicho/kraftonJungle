# https://www.acmicpc.net/problem/9935

# 시간초과

# import sys

# st = []

# input = str(sys.stdin.readline().rstrip())
# check = str(sys.stdin.readline().rstrip())

# cnt = 0
# idx = len(check)
# sub = ""

# for i in input:
#     if check.count(i) > 0:
#         cnt += 1
#         if cnt >= idx:
#             if (''.join((st[::-1])[0:idx]))[::-1] + i == check:
#                 for k in range(idx-1):
#                     st.pop()
#         else:
#             st.append(i)
#     else:
#         st.append(i)

# if len(st) > 0:
#     for j in st:
#         print(j,end="")

# else:
#     print("FRULA")


# 다른사람 참고

import sys

st = []

input = str(sys.stdin.readline().strip())
check = str(sys.stdin.readline().strip())

idx = len(check)

for i in input:
    st.append(i)       # 문자열 받은걸 하나씩 쪼개서 스택에 넣고

    print(st)
    #print("".join(st[len(input) - idx :]))

    if "".join(st[len(st) - idx :]) == check:  # 스택 끝에서 폭발문자열 길이만큼 잘라서 비교한 결과가 같으면
        for _ in range(idx):
            st.pop()  # 폭발 문자열 길이만큼 pop

if len(st) > 0:
    print("".join(st))
else:
    print("FRULA")