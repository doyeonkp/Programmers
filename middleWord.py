#https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    pos = len(s) // 2
    # even
    if len(s) % 2 == 0:
        return (s[pos-1:pos+1])
    # odd
    answer = s[pos]
    return answer
