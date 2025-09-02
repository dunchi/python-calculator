# calculator.py
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "0으로 나눌 수 없습니다!"
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    if x < 0:
        return "음수의 제곱근은 계산할 수 없습니다."
    return math.sqrt(x)

def sine(x):
    # 사용자가 도(degree) 단위로 입력하는 것을 가정하고 라디안으로 변환
    return math.sin(math.radians(x))

def cosine(x):
    # 사용자가 도(degree) 단위로 입력하는 것을 가정하고 라디안으로 변환
    return math.cos(math.radians(x))

def tangent(x):
    # 사용자가 도(degree) 단위로 입력하는 것을 가정하고 라디안으로 변환
    return math.tan(math.radians(x))

def log10(x):
    if x <= 0:
        return "0 또는 음수의 로그는 계산할 수 없습니다."
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "0 또는 음수의 로그는 계산할 수 없습니다."
    return math.log(x)


print("=== 파이썬 공학용 계산기 ===")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
print("5. 거듭제곱 (x^y)")
print("6. 제곱근")
print("7. 사인 (sin)")
print("8. 코사인 (cos)")
print("9. 탄젠트 (tan)")
print("10. 상용로그 (log10)")
print("11. 자연로그 (ln)")

while True:
    choice = input("원하는 연산을 선택하세요 (1-11, 종료하려면 'q' 입력): ")

    if choice.lower() == 'q':
        print("계산기를 종료합니다.")
        break

    # 두 개의 숫자가 필요한 연산
    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            print("-" * 20)
            continue

        if choice == '1':
            print("결과:", add(num1, num2))
        elif choice == '2':
            print("결과:", subtract(num1, num2))
        elif choice == '3':
            print("결과:", multiply(num1, num2))
        elif choice == '4':
            print("결과:", divide(num1, num2))
        elif choice == '5':
            print("결과:", power(num1, num2))

    # 한 개의 숫자만 필요한 연산
    elif choice in ['6', '7', '8', '9', '10', '11']:
        try:
            num = float(input("숫자를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
            print("-" * 20)
            continue

        if choice == '6':
            print("결과:", square_root(num))
        elif choice == '7':
            print("결과:", sine(num))
            print("(입력값은 각도(degree)로 처리됩니다)")
        elif choice == '8':
            print("결과:", cosine(num))
            print("(입력값은 각도(degree)로 처리됩니다)")
        elif choice == '9':
            print("결과:", tangent(num))
            print("(입력값은 각도(degree)로 처리됩니다)")
        elif choice == '10':
            print("결과:", log10(num))
        elif choice == '11':
            print("결과:", ln(num))
    else:
        print("잘못된 선택입니다. 1부터 11 사이의 숫자를 입력해주세요.")

    print("-" * 20)