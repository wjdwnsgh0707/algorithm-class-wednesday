#===================================================
# 알고리즘 설계 전략 : 분할과 정복 (DC: Dvide & Conquer)
#===================================================
# 1. k번쨰 작은수 찾는 문제(kth smnallest selection problem)
# - 최소 정복으로 설계, 퀵 정렬의 분할 함수 이용, 재귀함수로 처리
# (1) 분할함수
def partition(A, left, right):
    pivot = A[left]
    i = left + 1
    j = right
    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j
# (2) 축소정복 전략
def quick_select(A, left, right, k):
    if left == right:   # 재귀함수 호출 종료
        return A[left]
    pos = partition(A, left, right) # 피봇을 배열 A의 첫번째 요소로 설정
    if k + left == pos + 1 :    # case 1. 피봇이 k번째인 경우
        return A[pos]
    elif k + left < pos + 1 :   # case 2. k번째 작은 수가 왼쪽에 있는 경우
        return quick_select(A, left, pos -1, k)
    else:                       # case 3. k번쨰 작은 수가 오른쪽에 있는 경우
        return quick_select(A, pos +1, right, k - (pos + 1 - left))
    
# 테스트1
print("\t테스트 1 : 분할함수")
A = [7, 2, 1, 8, 6, 3, 5, 4, 0]
k = 3
print(quick_select(A, 0, len(A)-1, k))
print("="*100)

# 2. 병합정렬(MergeSort) 문제
# - 오름차순으로 정렬
# 1. 병합함수 (merge)
def merge(A, left, mid, right):
    # 1. 임시 리스트 생성 - 크기 = right - left + 1
    sorted_list = [0] * (right - left +1)
    # 2. 두 부분 리스트의 시작 인덱스
    i = left
    j = mid + 1
    k = 0
    # 3. 두 정렬 리스트를 비교하여 임시리스트에 기록
    while i <= mid and j <= right :
        if A[i] <= A[j]:
            sorted_list[k] = A [i]
            i += 1
            k += 1
        else:
            sorted_list[k] = A [j]
            j += 1
            k += 1
    # 4-1. 왼쪽 부분 리스트에 요소가 남아 있는 경우 -> 리스트에 모두 복사
    while i <= mid:
        sorted_list[k] = A [i]
        i += 1
        k += 1
    # 4-2. 오른쪽 부분 리스트에 요소가 남아 있는 경우 -> 리스트에 모두 복사
    while j <= right:
        sorted_list[k] = A [j]
        j += 1
        k += 1
    # 5. 임시 리스트의 결과를 원래 리스트 A에 덮어쓰기
    for t in range(k):
        A[left + t] = sorted_list[t]

# 2. 병합정렬 함수
def merge_sort(A, left, right):
    if left < right:    # 항목이 두개 이상인 경우에만 분할
        mid = (left + right) // 2
        merge_sort(A, left, mid)    # 왼쪽 서브리스트 병합정렬
        merge_sort(A, mid+1, right) # 오른쪽 서브리스트 병합정렬
        merge(A, left, mid, right)  # 정렬된 두 개의 부분 리스트를 병합

# 테스트2
print("\t테스트 2 : 병합정렬")
A = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", A)
merge_sort(A, 0, len(A) - 1)
print("정렬 후:", A)
print("="*100)

#====================================================
#알고리즘 설계 전략: 동적 계획법(DP; Dynamic Programming)
#====================================================
# 1. 피보나치 수열 문제 (fibonacci sequence)
# 1-1. 메모이제이션 방식(top-down, 하향식) - 주어진 문제를 작은 문제로 해결해 나가는 방신
# 1. 전역 변수로 DP 1차원 배열로 구현
mem = [None] * 11
# 피보나치 수 계산하기
def fib_dp_mem(n):      # fib(n) = ?
    if mem[n] is None:  # 처음 계산
        if n < 2:   #재귀 함수 호출 종료
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

# 테스트3
print("\t테스트 3 : 피보나치 수열")
print("n = 6 -> fib(6):", fib_dp_mem(6))
print("mem =", mem[:7]) # 결과 수열 출력
print("="*100)

# 1-2. 테이블화 방식(bottom-up, 상향식) - 작은 문제부터 해결하여 주어진 문제를 해결
def fib_dp_tab(n):      # fib(n) = ?
    # 1. 테이블 - 1차원 리스트
    table = [None] * (n+1)
    table[0] = 0
    table[1] = 1
    # 2. n >= 2 이상인 경우
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table
# 테스트4
print("\t테스트 4 : 피보나치 수열(테이블화)")
table = fib_dp_tab(8)
print("fib(6) ==>",table[8])
print("fib.seq ==>", table[:9])
print("=" * 100)

#====================================================================
# 프로그래밍 문제 : 계단 오르는 방법의 수 계산하기 - 피보나치 수열 점화식 이용!
#====================================================================

# 2. 0/1 배낭 문제 DP 구현 - 물건의 개수는 n, 배낭의 용량은 W
# DP 테이블 A[i][w] (주어진 남아있는 배낭 용량 w에서 1부터 i 물건을 까지 고려했을 때 얻어지는 배낭의 최대 가치)을 완성.
# 최종 출력값 A[n][W]는 "최대 가치"만 알려줄 뿐, 어떤 물건들을 선택해야 이 값을 만들 수 있는지 알려주지 않음.
"""
동작 방식 요약 : 
1. i: 위에서 아래로, 물건 1개 → n개
2. w: 왼쪽에서 오른쪽으로, 용량 0 → W
3. 각 칸에서 현재 물건의 무게와 남아 있는 배낭의 용량의 크기을 비교해서
- 넣을 수 없으면 위 값 복사
- 넣을 수 있으면
    - 넣는 경우
    - 안 넣는 경우 
    → 더 큰 값으로 갱신
4. 테이블 오른쪽 아래 A[n][W]가 최종 해답
"""
def knapSack_dp(W, wt, val, n):
    # 1. DP 테이블 초기화 : (n+1) X (W + 1)
    A = []
    for i in range(n + 1):          # 행 생성 (0 ~ n)
        row = []
        for w in range(W + 1):      # 열 생성 (0 ~ W)
            row.append(0)           # 모든 값을 0으로 초기화
        A.append(row)

    # 2. DP 테이블 채우기
    for i in range(1, n + 1):       # 물건 index 1~n - 위에서 아래로 진행
        for w in range(1, W + 1):   # 배낭 용량 1~W - 좌에서 우로 진행
            if w < wt[i-1]:         # i번째 물건이 용량 초과해서  넣을 수 없으므로 위 값 복사
                A[i][w] = A[i-1][w]
            else:                   # i번째 물건을 넣을 수 있으면
                valWith = val[i-1] + A[i-1][w - wt[i-1]]  # 넣는 경우
                valWithout = A[i-1][w]                    # 빼는 경우
                A[i][w] = max(valWith, valWithout)        # 더 큰 값을 선택
    
    # 3. 최대 가치와 DP테이블 A 둘 다 반환
    return A[n][W], A


# 테스트 
n = 3
wt = [2, 1, 3]
val = [12, 10, 20]
W = 5

max_value, A = knapSack_dp(W, wt, val, n)

print("1. 최대 가치 =", max_value)
print()
print("2. DP table")
for i in range(4):
    for w in range(6):
        print(A[i][w],  end = "   ")
    print()

print()
print("3. 선택된 물건 역추적 기능")
"""
선택된 물건의 무게만큼 용량을 줄이고, DP 테이블에서 위로 올라가며 계속 확인한다.
"""
selected = []
w = W
# 물건 데이터
items = [("item1", 2, 12), ("item2",1, 10),("item3",3, 20)]

for i in range(n, 0, -1): # DP 테이블을 거꾸로 올라가며 선택된 물건을 하나씩 찾아내는 과정이 필요
    if A[i][w] != A[i-1][w]:         # i번째 물건은 선택되어 가방에 들어감
        name, wt, val = items[i-1]   # i번째 물건을 리스트에 추가
        selected.append(name)  
        w -= wt                      # i번째 물건을 배낭에 넣었으므로 배낭의 용량에서 그 무게만큼 줄어든다.
                                     # 줄어든 나머지 용량 w에서 앞선 물건(i-1번째까지)으로 최대 가치를 만드는 방법 고려
    else:
        pass

selected.reverse()
print("선택된 물건:", selected)