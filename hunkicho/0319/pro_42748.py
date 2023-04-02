# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in commands:
        get_list = array[i[0] - 1:i[1]]
        get_list.sort()
        print(get_list[i[2]])
        
        #answer.append(get_list[i[2]])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	)