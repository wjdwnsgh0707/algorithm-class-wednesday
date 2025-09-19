#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 정준호
#  작성일: 2025-09-19
# 순환(recursion)과 반복(iteration)의 차이점 이해
#  - 반복문 기반과 재귀 기반의 팩토리얼 계산 함수 구현
#  - 유효성 검사 포함 (0 이상 정수 확인)
#  - 문자열 입력 → 정수 변환 → 유효성 검사 → 팩토리얼 계산까지 포함된 콘솔 프로그램 형태
#  - q 또는 quit 입력 시 종료
#############################################################################
def factorial_iter(n):
    # 반복문 기반 n!
    result = 1
    for k in range(2, n+1):
        result *= k
    return result

def factorial_rec(n):
    # 재귀적으로 문제 해결 n! -> 재귀함수 정의
    # 1. base case(재귀 호출 종료 조건)
    if n == 1:
        return 1
    # 2. 재귀 분할 호출
    return n * factorial_rec(n-1)

# 메인 함수 def

if __name__ == "__main__":
    while True:
        n = int(input("\n정수를 입력하세요: ").strip())

        # 종료 조건
        if n.lower() in ("q", "quit"):
            print("프로그램을 종료합니다.")
            break

        # 숫자 확인
        if not n.isdigit():
            print("올바른 정수를 입력하세요.")
            continue

        # 음수 처리
        if n < 0:
            print("0 이상의 정수를 입력해야 합니다.")
            continue

        print(f"반복문 기반: {factorial_iter(n)}")
        try:
            print(f"재귀 기반: {factorial_rec(n)}")
        except RecursionError:
            print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main()
