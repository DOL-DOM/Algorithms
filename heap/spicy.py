#스코빌 지수 가장 낮은 두개를 섞어서 (a+2b), 모든게 k이상일때까지 섞기
#스코빌 지수를 담은 배열 scoville, 원하는 스코빌 지수 K 주어짐
#몇 번 섞는지, 최소 횟수 리턴 solution 함수

import sys
from heapq import heappush, heappop

#리스트를 받을 때 그냥 이렇게 이름만 쓰면 되나?
def solution(scoville, K):
    food = []
    num = 0
    #1. 가진 음식들, 최소 힙 정렬 (1)heapify -시간 복잡 (2)heappush()
    for i in range(0,len(scoville)):
        heappush(food, scoville[i])

    #2. 가진 음식 중 최소 2개를 반복해서 섞음. 제일 작은게 k 넘을 때까지
    while (food[0] < K):
        try:
            heappush(food, heappop(food) + (heappop(food)*2)) 
            num +=1
        except IndexError:
            return -1
            
        
    return num

scoville = [1, 2, 3, 9, 10, 12]
K=7
print(solution(scoville, K))