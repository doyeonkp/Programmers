#https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    cnt = 0
    last = ""
    for i, c in enumerate(arr):
        if c == last:
            continue;
        else:
            answer.append(c)
            last = c
    return answer
