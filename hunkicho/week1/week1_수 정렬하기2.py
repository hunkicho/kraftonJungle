# https://www.acmicpc.net/problem/2751
# https://www.acmicpc.net/board/view/31887

# 박찬우님의 코드

import sys
n = int(sys.stdin.readline())
number_list = [[0] for i in range(2000001)]
#print("input=",number_list)

for i in range(n) :
    input_number = int(sys.stdin.readline())
    number_list[input_number + 1000000][0] = 1
    #print("number_list=",number_list)

for i in range(2000001) :
    if (number_list[i][0] == 1) :
        print("i=",i)
        print("number_list[i][0]=",number_list[i][0])
        print(i-1000000)