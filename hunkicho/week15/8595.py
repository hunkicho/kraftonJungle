# https://www.acmicpc.net/problem/8595


# 이게 왜 틀린건지 잘 모르겠다...
import sys

if __name__ == "__main__":
    word_lenth = int(sys.stdin.readline())
    word = list(sys.stdin.readline().strip())
    number = ""
    number_hap = 0

    for i in word:
        if i.isdecimal():
            
            if len(number) == 6:
                number_hap += int(number)
                number = ""
            number += i
        else:
            if number != "":
                number_hap += int(number)
                number = ""
    if len(number) != 0 and len(number) < 6:
                number_hap += int(number)
    
    print(number_hap)


# 인터넷에서 본 답 

# import sys

# if __name__ == "__main__":
#     word_lenth = int(sys.stdin.readline())
#     word = list(sys.stdin.readline().strip())
#     number = ""
#     number_hap = 0

#     for i in word:
#         if i.isdecimal() == False:
#             if len(number) < 7 and len(number) != 0:
#                 number_hap += int(number)
#             number = ""
#             continue
#         number += i
#     if len(number) < 7 and len(number) != 0:
#         number_hap += int(number)
#     print(number_hap)