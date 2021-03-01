#https://programmers.co.kr/learn/courses/30/lessons/12918#
def solution(s):
    if not (len(s) == 4) and not (len(s) == 6):
        return False
    if s.isnumeric():
        return True
    return False
