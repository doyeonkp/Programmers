#-*- encoding: utf-8 -*-
# 2019 카카오 개발자 겨울 인턴쉽
# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

# board : [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves : [1,5,3,5,1,2,1,4]
# result = 4

def solution(board, moves):
    que = []
    answer = 0
    claw = 0
    # board로 들어오는 list들은 가로줄 베이스임으로, 세로줄로 새로 묶어서
    # 새 맵으로 저장
    # list comprehension 이용
    # zip(*iterables) => zip('ABCD', 'xy') --> Ax By
    new_map = [list(i) for i in zip(*board)]
    
    for i in range(len(moves)):
	# move가 가르키는 위치
        pos = moves[i] - 1

	# 새로 만든 list에 post번째의 list가 존재 할때까지
        while new_map[pos]:
	    #pop(0) 으로 popleft와 같은 로직으로 작동
            claw = new_map[pos].pop(0)
            if claw == 0:
                continue;
            if claw != 0:
                if len(que) > 0 and que[-1] == claw:
                    que.pop()
		    # pop은 1번만 하지만, 새로 찾은 claw를 큐에 넣지 않기 때문에
		    # 인형은 총 pop한 1개, 큐에 넣지 않은 claw 1개로 총 2개이기 때문에
		    # 2개씩 갯수를 증가해 카운트한다.
                    answer += 2
                else:
                    que.append(claw)
                break;

    return answer
