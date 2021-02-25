#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * (n+2)
    for i in reserve:
        clothes[i] += 1
    for i in lost:
        clothes[i] -= 1

    for i in range(1, n+1):
        if clothes[i-1] == 0 and clothes[i] == 2:
            clothes[i-1], clothes[i] = 1,1
        elif clothes[i] == 2 and clothes[i+1] == 0:
            clothes[i], clothes[i+1] = 1,1

    answer = len([x for x in clothes if x>0]) - 2
    return answer
