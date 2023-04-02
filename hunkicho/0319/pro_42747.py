# https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 인터넷 봤다

def solution(citations):
    citations.sort()
    
    for i in range(len(citations), -1, -1):
        print(i, citations[-i])
        if citations[-i] >= i:
            return i
        
solution([3, 0, 6, 1, 5])