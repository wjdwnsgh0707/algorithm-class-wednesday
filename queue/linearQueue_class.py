# linearQueue_class.py
#############################################################
# 배열을 이용한 선형 큐 구현
#  - front: '첫 번째 요소 바로 이전(앞)'의 인덱스 
#   - rear:  '마지막 요소'의 인덱스
# - 기본적인 큐 연산: enqueue, dequeue, is_empty, is_full, size, peek
# - 큐의 용량 : capacity
# - 빈 큐 : front = -1, rear = -1
# - 포화 상태 큐 : rear = capacity - 1
# 작성자: 정준호
# 작성 날짜: 2025/09/18
#############################################################

# 원형큐는 front -1 값이 필요 없다. (선형 큐랑 달리)
# 선형 큐에서는 모듈러 연산 X / self.front = (self.front + 1) / 3주차 pdf 참고
class LinearQueueNoReset:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            raise Exception("큐가 가득 찼습니다.")
        self.rear += 1
        self.array[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("큐가 비어 있습니다.")
        self.front += 1
        return self.array[self.front]

    def peek(self):
        if self.is_empty():
            raise Exception("큐가 비어 있습니다.")
        return self.array[self.front + 1]

    def size(self):
        return self.rear - self.front

    # 출력
    def display(self, msg="LinearQueueNoReset"):
        """큐의 상태를 출력"""
        
        print(f"{msg}: front={self.front}, rear={self.rear},\
              size={self.size()}/{self.capacity}", end="  |  ")

        # 전체 슬롯(0..capacity-1)을 순서대로 출력
        # active 구간(front < i <= rear)은 실제 값, 그 외는 None로 표시
        print("[", end="")
        for i in range(self.capacity):
			if (self.front < i <= self.rear):
				val = self.array[i] 
			else:
				val = None
             print(val, end=" ")
    	print("]")



# =======================================================
# (그림 2.5 :Enqueue 5회, Dequeue 2회 후 다시 Enqueue 시도)
# =======================================================
def test_fig_2_5_demo():
    print("=== Fig. 2.5 데모 (리셋 없는 선형 큐) ===")
    q = LinearQueueNoReset(capacity=5)
    q.display("초기")    

    # 1) enqueue 5회 (가득)
    for x in "ABCDE":
        q.enqueue(x)
    q.display("enqueue 5회 후")    

    # 2) dequeue 2회 → front=1, rear=4
    for _ in range(2):
        q.dequeue()
    q.display("dequeue 2회 후") 
    
    # 3) 다시 enqueue 1회 시도 → rear가 이미 끝에 있어 is_full() → 예외처리
    try:
        q.enqueue("F")
    except Exception as e:
        print("False Full 예외 발생:", "-", e)    
    


if __name__ == "__main__":
    test_fig_2_5_demo()
	input("\n엔터를 누르면 종료 됩니다.")
    
    



    
