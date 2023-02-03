# https://www.acmicpc.net/problem/1062

# 못풀겠다

# import sys

# if __name__ == "__main__":
#     first = set(list('anta') + list('tica'))
#     input_list = []
#     count = 0
#     n, k = map(int, sys.stdin.readline().split())

#     for _ in range(n):
#         word = set(list(sys.stdin.readline().rstrip()))
#         remains = word - first
#         input_list.append(remains)

#     for i in input_list:
#         if len(i) + len(first) <= k:
#             count += 1
#     print(count)



# 다른사람 봄
# 이거는 비트마스킹 안쓴거
# from itertools import combinations 
# import sys
# n, k = map(int, input().split())
# answer = 0
# # a,n,t,i,c는 반드시 가르쳐야 함

# first_word = {'a','n','t','i','c'}

# remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word  # 남은 알파벳들
# data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]      # 입력한 단어들에서 필수 알파벳 뺸 나머지

# def countReadableWords(data, learned):
#    cnt = 0
#    for word in data:
#       canRead = 1
#       for w in word:
#           # 안배웠으니까 못읽는다.
#          if learned[ord(w)] == 0:
#             canRead = 0
#             break
#       if canRead == 1:
#          cnt += 1
#    return cnt

# if k >= 5:
#    learned = [0] * 123
#    for x in first_word:
#       learned[ord(x)] = 1

#    # 남은 알파벳 중에서 k-5개를 선택해본다.
#    for teach in list(combinations(remain_alphabet, k-5)):
#       for t in teach:
#          learned[ord(t)] = 1
#       cnt = countReadableWords(data, learned)

#       if cnt > answer:
#          answer = cnt
#       for t in teach:
#          learned[ord(t)] = 0
#    print(answer)
# else:
#    print(0)


# 또 다른 사람 거
import sys

n, k = map(int, input().split())

# k 가 5보다 작으면 어떤 언어도 배울 수 없음
if k < 5:
    print(0)
    exit()
# k 가 26이면 모든 언어를 배울 수 있음
elif k == 26:
    print(n)
    exit()

answer = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1


def dfs(idx, cnt):
    print(idx, cnt)
    global answer

    if cnt == k - 5:
        readcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


dfs(0, 0)
print(answer)