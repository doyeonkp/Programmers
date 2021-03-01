#https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    multiply, result = 1,0
    while n > 0:
        result += n % 3 * multiply
        multiply *= 10
        n = n // 3
    base3Num = str(result)[::-1]
    return(int(base3Num, 3))
