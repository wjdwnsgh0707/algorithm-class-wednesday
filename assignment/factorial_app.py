import time

def factorial_iter(n):
    if n < 0:
        raise ValueError("음수는 입력할 수 없습니다.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n):
    if n < 0:
        raise ValueError("음수는 입력할 수 없습니다.")
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def main():
    while True:
        print("\n1. 반복문 방식")
        print("2. 재귀 방식")
        print("3. 둘 다 비교")
        print("0. 종료")
        choice = input("선택: ")

        if choice == "0":
            print("종료합니다.")
            break

        n_str = input("정수 입력: ")
        try:
            n = int(n_str)
        except:
            print("정수를 입력하세요.")
            continue

        if choice == "1":
            try:
                result, elapsed = run_with_time(factorial_iter, n)
                print(f"결과: {result}")
                print(f"시간: {elapsed:.6f}초")
            except Exception as e:
                print("오류:", e)

        elif choice == "2":
            try:
                result, elapsed = run_with_time(factorial_rec, n)
                print(f"결과: {result}")
                print(f"시간: {elapsed:.6f}초")
            except Exception as e:
                print("오류:", e)

        elif choice == "3":
            try:
                iter_result, iter_time = run_with_time(factorial_iter, n)
                rec_result, rec_time = run_with_time(factorial_rec, n)
                print(f"[반복] 결과: {iter_result} / 시간: {iter_time:.6f}초")
                print(f"[재귀] 결과: {rec_result} / 시간: {rec_time:.6f}초")
            except Exception as e:
                print("오류:", e)

        else:
            print("올바른 번호를 선택하세요.")

if __name__ == "__main__":
    main()