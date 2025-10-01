#===========================================================
# 코드 3.4 : 이중 연결 구조를 위한 Node 클래스 
"""
1. 이중 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드와 두 개의 링크 필드를 가짐
3. 링크 필드는 각각 이전 노드와 다음 노드를 가리킴
4. 이 구조는 양방향 탐색이 가능하게 함
5. 노드 생성 시 데이터와 링크 필드를 초기화
7. 링크 필드는 기본적으로 None으로 설정
8. 주요 메서드:
    - append(node) : 새로운 노드를 현재 노드 뒤에 삽입
    - popNext() : 현재 노드 뒤에 있는 노드 삭제
"""
# 이중연결 Node 클래스
# 이중 연결 노드 클래스
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


# 이중 연결 리스트 클래스
class DLinkedList:
    def __init__(self):
        self.head = None  # 첫 노드

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return False  # 파이썬은 메모리 부족 전까지는 full이 아님

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        for _ in range(pos):
            if node is None:
                return None
            node = node.next
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        return None if node is None else node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node:
            node.data = elem
        else:
            raise IndexError("잘못된 위치입니다")

    def insert(self, pos, elem):
        new_node = DNode(elem)
        if pos == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        prev = self.getNode(pos - 1)
        if prev is None:
            raise IndexError("삽입 위치 오류")

        new_node.next = prev.next
        new_node.prev = prev
        if prev.next:
            prev.next.prev = new_node
        prev.next = new_node

    def delete(self, pos):
        if pos < 0 or self.head is None:
            raise IndexError("삭제 위치 오류")

        if pos == 0:
            deleted = self.head
            self.head = deleted.next
            if self.head:
                self.head.prev = None
            return deleted

        prev = self.getNode(pos - 1)
        if prev is None or prev.next is None:
            raise IndexError("삭제 위치 오류")

        deleted = prev.next
        prev.next = deleted.next
        if deleted.next:
            deleted.next.prev = prev
        return deleted

    def find(self, elem):
        index = 0
        node = self.head
        while node:
            if node.data == elem:
                return index
            node = node.next
            index += 1
        return -1

    def display(self, msg="DLinkedList:"):
        print(msg, end=' ')
        node = self.head
        while node:
            print(node.data, end=' <-> ')
            node = node.next
        print("None")

#=========================================================
# 코드 3.5: 이중연결리스트 클래스
"""
1. 이중 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드:
    -동일 연산
        - isEmpty(): 리스트가 비어있는지 확인
        - isFull(): 리스트가 가득 찼는지 확인
        - getEntry(pos): 특정 위치의 노드 데이터를 반환
        - replace(pos, elem): 특정 위치의 노드 데이터를 변경 
    - getNode(pos): 특정 위치의 노드를 반환
    - size(): 리스트의 크기를 반환
    - display(msg): 리스트의 내용을 출력
    - insert(pos, elem): 특정 위치에 새 노드를 삽입
    - 나머지 연산
        - delete(pos): 특정 위치의 노드를 삭제
        - find(elem): 특정 데이터를 가진 노드를 검색
"""
#=========================================================
# 코드 3.3 단순연결리스트 테스트 프로그램   
#========================================================
#1. 연결 리스트 생성
ll = DLinkedList()
ll.display("연결리스트(초기):   ")      # 출력: LinkedList: None

#2. 노드 삽입
ll.insert(0, 10) # 첫 번째 위치에 10 삽입
ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
ll.insert(1, 30)  # 두 번째 위치에 30 삽입
ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
ll.insert(2, 50)  # 세 번째 위치에 50 삽입
ll.display("연결리스트(삽입x5): ")     # 출력: LinkedList: 20->30->50->10->40->None 
ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
ll.display("연결리스트(교체X1-> 90으로 변경): ")     # 출력: LinkedList: 20->30->90->10->40->None

# 3.노드 삭제
ll.delete(2)      # 세 번째 노드 삭제
ll.delete(3)      # 네 번째 노드 삭제
ll.delete(0)      # 첫 번째 노드 삭제
ll.display("연결리스트(삭제x3): "   )      # 출력: LinkedList: 30->10->None



