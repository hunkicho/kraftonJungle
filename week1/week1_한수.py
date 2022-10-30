# https://www.acmicpc.net/problem/1065

# 1자리랑 2자리인거 포함 안함
# # import sys
# input_number = int(sys.stdin.readline())

# if input_number <= 9:
#     print("len",len(input_number))
#     print(9)
# elif input_number <= 99:
#     print(len(input_number))
#     print(99)
# else:
#     if int(str(input_number)[0:1])  % 2 == 0:
#         print("first1,",str(input_number)[0:1] )
#         print((int(str(input_number)[0:1]) // 2) * 2)
#     else:
#         print("first2,",str(input_number)[0:1] )
#         print(( ( int(str(input_number[0:1])) // 2) * 2) + 1)


import sys
input_number = int(sys.stdin.readline())

# all = 0
# def sum(n):
#     sum = 0
#     for i in range (n,0,-1):
#         if i % 2 == 0:
if input_number <= 98:
    print(input_number)
elif input_number <= 110:
    print(99)
else:
    sum = 0
    if input_number >= int(str(input_number)[0:1]*3):
        sum += 1
    








# 9 5 4 
# 8 4 0
# 7 4 1
# 6 3 0
# 5 3 1
# 4 2 0
# 3 2 1
# 2 1 0
# 1 1 1