def validate_resident_number(resident_number):
    # 입력된 주민등록번호의 길이가 13자리가 아니거나 숫자가 아닌 경우 유효하지 않음
    if len(resident_number) != 13 or not resident_number.isdigit():
        return False

    # 각 자리수에 곱해질 계수들
    factors = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    total = 0

    # 주민등록번호의 각 자리수를 계수와 곱하고 총합을 계산
    for i in range(12):
        total += int(resident_number[i]) * factors[i]

    # 총합을 11로 나눈 나머지를 계산하여 유효성 검증 코드를 구함
    remainder = total % 11
    check_digit = 11 - remainder if remainder != 0 else 0

    # 계산된 유효성 검증 코드가 주민등록번호의 마지막 자리수와 일치하면 유효함
    return check_digit == int(resident_number[-1])

# 주민등록번호 입력 받기
resident_number = input("주민등록번호를 입력하세요: ")

# 유효성 검사
if validate_resident_number(resident_number):
    print("주민등록번호가 유효합니다.")
else:
    print("주민등록번호가 유효하지 않습니다.")
