#https://programmers.co.kr/learn/courses/30/lessons/68644#
def solution(numbers):
    temp = []
    for i in range(len(numbers)-1):
        answer = []
        num = numbers[i]
        j = i+1
        while j < len(numbers):
            sum_T = num + numbers[j] 
            temp.append(sum_T)
            j += 1

    answer = list(set(temp))
    answer.sort()
    return answer
