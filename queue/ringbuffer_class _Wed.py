# ringbuffer_class.py
# 링 버퍼의 주요 특징:
#   - 고정 크기: 미리 정의된 크기를 가지며, 초과 시 덮어쓰기.
#   - 빠른 삽입/삭제: O(1) 시간 복잡도로 데이터 추가 및 제거 가능.
#   - 링 버퍼는 큐와 유사하지만, 큐는 데이터가 가득 찼을 때 추가 삽입이 불가능.
#   - 반면 링 버퍼는 덮어쓰기 기능을 통해 새로운 데이터를 계속해서 추가할 수 있음.

from circular_queue_class import CircularQueueOneSlotEmpty
class RingBuffer:
    def __init__(self, capacity):
        # 내부 배열에 한 칸 비움 방식의 링버퍼
        self.q = CircularQueueOneSlotEmpty(capacity=capacity)

    def is_empty(self):
        return self.q.is_empty()
    
    def is_full(self):
        return self.q.is_full()
    
    def peek(self):
        return self.q.peek()
    
    def size(self):
        return self.q.size()
    
    def display(self, msg="RingBuffer: "):
        return self.q.display(msg + "내부 링버퍼의 상태")
    
    def read(self):
        # 링버퍼에서 가장 오래된 데이터를 삭제
        return self.q.dequeue()
    
    def enqueue2(self, item):
        # 링버퍼에 포화상태일 때 새 데이터를  삽입 연산
        q = self.q
        q.rear = (q.rear + 1) % q.N
        if q.rear == q.front: # full 이면( 원형 큐인 경우 오버플로우 발생 )
            q.front = (q.front + 1) % q.N # overwrite 발생( 가장 오래된 데이터 drop )
        q.array[q.rear] = item # 데이터 기록

#===============================
# 링버퍼 테스트 프로그램
# =============================

def test_code_2_3():
    rb = RingBuffer(capacity=8)  # 실제 저장 가능 개수 = 8 (N=9)
    rb.display("초기 상태")
    print()

    # 0..5 기록(아직 full 아님)
    for x in range(6):
        rb.enqueue2(x)           # = rb.write(x) 와 동일한 효과 ( 신경 X )
    rb.display("삽입 0-5 후")
    print()

    # 6 기록
    rb.enqueue2(6)
    rb.display("6 삽입 후")
    print()

    # 7 기록 후 → 정확히 full
    rb.enqueue2(7)
    rb.display("7 삽입 후")
    print()

    # 포화 상태에서 8 기록 → 가장 오래된 0 drop → [1..8]
    rb.enqueue2(8)
    rb.display("8 삽입 후 (overwrite)")
    print()

    # 포화 상태에서 9 기록 → 가장 오래된 1 drop → [2..9]
    rb.enqueue2(9)
    rb.display("9 기록 후 (overwrite)")
    print()

    # 두 개 읽기 → 2, 3
    print("read:", rb.read(), rb.read())
    rb.display("2개 읽은 후")
    print()

def quiz_3():
    """ 
    capacity가 8인 원형큐를 링버퍼로 사용하는 경우, 공백상태의 큐에 1,2,3,..., 20의 정수를 \
        순서대로 삽입하여 큐에 남은 요소 관련 정보 출력하시오.
    """
    print("\n=== quiz_3 ===")

    # 1. capacity가 8인 링버퍼 생성
    rb = RingBuffer(capacity = 8)
    rb.display("초기 링버퍼 상태")

    # 2. 공백 상태의 링버퍼에 1,2,3, ... , 20의 정수를 순서대로 삽입
    for i in range(1, 21):
        rb.enqueue2(i)
        print(i, end = " ")
        rb.display("삽입 후 :")

    # 3. 링버퍼에 남은 요소 관련 정보 출력
    print(f"front = {rb.q.front}, rear = {rb.q.rear}, size = {rb.q.size()} / {rb.q.capacity}")

if __name__ == "__main__":
    # test_code_2_3()
    quiz_3()