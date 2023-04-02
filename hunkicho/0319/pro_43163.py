# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])

    
    
    while q:
        
        word, count = q.popleft()
        print(word, count)
        
        if word == target:
            return count
        for i in words:
            for j in range(len(i)):
                first = word[:j] + word[j+1:]
                last = i[:j] + i[j+1:]
                if first == last:
                    q.append([i, count + 1])
                    
    return 0

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])