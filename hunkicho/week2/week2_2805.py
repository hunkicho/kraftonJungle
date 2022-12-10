# https://www.acmicpc.net/problem/2805

# import sys
# count, length = list(map(int, sys.stdin.readline().split()))
# tree = list(map(int, sys.stdin.readline().split()))
# cut = 0

# tree.sort(reverse=True)

# for i in range(len(tree)):
#     cut += tree[i] - tree[i+1]
#     if cut >= length:
#         if cut == length:
#             print(tree[i+1])
#         else:
#             print(tree[i+1] + (cut - length))
#         break
    

# import sys

# def bin_search(arr, src):
#     pl = 0
#     pr = max(arr)
    

#     while pl <= pr:
#         pc = (pl + pr) // 2
#         hap = 0


#         for i in arr:
#             if i > pc:
#                 hap += i - pc
#         print("pl=",pl,"pr=",pr,"pc=",pc,"hap=",hap)

#         if hap > src:
#             pl += 1
#         else:
#             pr -= 1
#     print(pr)

# count, length = list(map(int, sys.stdin.readline().split()))
# tree = list(map(int, sys.stdin.readline().split()))

# cut = 0

# tree.sort()
# bin_search(tree,length)


# n,m =map(int,sys.stdin.readline().split())
# lis = list(map(int, sys.stdin.readline().split()))

# le=1
# ri=max(lis)

# while le<=ri:
#     mid = (le+ri)//2
#     total= [tree-mid if tree>mid else 0 for tree in lis]
#     # print(total)
#     total_val = sum(total)
#     # for tree in lis:
#     #     if tree>mid:
#     #         total+=(tree-mid)
#     if total_val>=m:
#         le=mid+1
#     else:
#         ri=mid-1

# print(ri)    



# 2022-11-25에 풀었다
# 근데 시간이 너무길다


# 처음 풀었을 때 틀렸는데 이유는 
# 5 23
# 50 32 48 28 10
# 위와 같이 찾으려는 값이 딱 떨어지지 않는 경우를 생각 못함
# 그래서 sum > key에서 기준값을 리스트에 넣고 나중에 최대값 출력


from typing import Any, Sequence
import sys

rtn_group = []

def bin_search(a: Sequence, key: Any) -> int:
    # 시퀀스 a에서 key와 일치하는 원소를 이진검색
    pl = 0
    pr = max(a)
    sum = 0
    global rtn_group 
    #print("max=",max(a))

    while True:
        pc = (pl + pr) // 2  # 중앙 원소의 인덱스
        #print("pl=", pl)
        #print("pr=", pr)
        #print("pc=", pc)
        for i in a:
            if i <= pc:
                num = 0
            else:
                num = i - pc
            #print("num=", num)
            sum += num

        #print("sum=",sum)
        #print("###############")

        if sum == key:
            return pc        # 검색 성공
        elif sum > key:
            pl = pc + 1      # 검색 범위를 뒤쪽 절반으로 좁힘
            rtn_group.append(pc)
        else:
            pr = pc - 1      # 검색 범위를 앞쪽 절반으로 좁힘
        
        if pl > pr:
            break
        sum = 0
            
    return -1

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    tree = list(map(int, sys.stdin.readline().split()))

    test = bin_search(tree, m)
    
    if test == -1:
        print(max(rtn_group))
    else:
        print(test)