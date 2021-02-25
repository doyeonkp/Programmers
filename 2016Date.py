#https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    cla_dic = {1:31,2:29,3:31,
              4:30,5:31,6:30,
              7:31,8:31,9:30,
              10:31,11:30,12:31}
    dates = ["FRI","SAT","SUN","MON","TUE","WED","THU"]

    for i in range(1,a):
        b += cla_dic[i]
    dIndex = b%7

    return dates[dIndex-1]
