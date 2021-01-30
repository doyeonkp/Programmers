#-*- encoding: utf-8 -*-
# 해당 문제는 해쉬 문제를 베이스로 하여,
# 해쉬 알고리즘을 응용해 풀어도 되지만,
# Counter 또한 연습해볼 수 있는 좋은 문제이다.
# 해당 문제에서는 Counter만 사용하지만, 다른 문제에서는 most_common이라는 메서드도
# 사용해 볼수 있다. Counter('hello world').most_common()을 하게 되면,
# 많이 나오는 글자 순으로 딕션너리가 반환되고, most_common(숫자)를 하게되면
# 숫자만큼 자주 나온 글자를 반환한다

# @Author: Doyeon M Kim

# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter as C


# participant : [marina, josipa, nikola, vinko, filipa]
# completion : [josipa, filipa, marina, nikola]
# return = vinko
def solution(participant, completion):
    # Counter를 사용하여, 단어의 갯수를 세어,
    # 해당 갯수가 몇개가 존재하는지를 dict형태로 반환
    # eg) 'hello world' -> {'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    answer = C(participant) - C(completion)
    return list(answer.keys())[0]
