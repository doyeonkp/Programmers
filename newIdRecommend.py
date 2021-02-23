#https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
import re
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9\_\.\-]', '', new_id)
    new_id = re.sub(r'\.\.+','.',new_id)
    new_id = new_id.strip(".")
    answer = new_id
    if answer == "":
        answer = "aaa"
    if len(answer) > 15:
        answer = new_id[0:15]
        answer = answer.strip(".")
    while len(answer) < 3:
        answer += answer[-1:]
        
    return answer
