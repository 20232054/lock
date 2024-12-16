import random

# 사용자 입력 검증 함수
def getValidatedInput(prompt, valid_range=None):
    """
    사용자 입력을 검증하는 함수.
    - prompt: 입력 요청 메시지
    - valid_range: 유효한 입력값의 범위 (리스트나 튜플)
    """
    while True:
        try:
            user_input = int(input(prompt))  # 사용자 입력을 정수로 변환
            if valid_range and user_input not in valid_range:  # 범위 검증
                print(f"Error: {valid_range[0]}에서 {valid_range[-1]} 사이의 숫자를 입력하세요.")
                continue
            return user_input  # 유효한 입력 반환
        except ValueError:
            print("Error: 숫자를 입력하세요.")  # 정수가 아닌 경우 예외 처리

# 비밀번호 생성 함수
def generatePassword(strength="중간", include_chars="", exclude_chars=""):
    """
    보안등급에 따라 비밀번호를 생성하며, 사용자가 지정한 문자를 포함하거나 제외할 수 있습니다.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*"

    # 보안등급별 길이 범위 정의
    length_ranges = {
        "약함": (5, 6),
        "중간": (7, 8),
        "강함": (9, 11)
    }

    # 보안등급에 따른 길이 설정
    length = random.randint(*length_ranges[strength])

    # 기본 문자 풀 생성
    char_pool = alphabet + alphabet.upper() + "0123456789" + special_characters

    # 제외할 문자를 필터링
    for char in exclude_chars:
        char_pool = char_pool.replace(char, "")

    # 비밀번호 생성
    password = ''.join(random.choice(char_pool) for _ in range(length))

    # 사용자가 포함하고 싶은 문자를 추가
    password += include_chars

    # 강함 등급일 경우 특수문자와 대문자를 반드시 포함
    if strength == "강함":
        password = replaceWithSpecialCharacter(password)
        password = replaceWithUppercaseLetter(password)

    # 비밀번호를 랜덤하게 섞기
    return ''.join(random.sample(password, len(password)))
    return password

# 비밀번호에 특수문자를 추가
def replaceWithSpecialCharacter(password):
    special_characters = "!@#$%^&*"
    replace_index = random.randrange(len(password))
    return password[:replace_index] + random.choice(special_characters) + password[replace_index + 1:]

# 비밀번호에 대문자를 추가
def replaceWithUppercaseLetter(password):
    replace_index = random.randrange(len(password))
    return password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]

# 비밀번호 보안등급 평가
def evaluatePasswordStrength(password):
    """
    비밀번호의 보안등급(약함, 중간, 강함)을 평가하는 함수.
    - 강함: 길이 ≥ 9, 숫자 ≥ 2, 대문자 ≥ 2, 특수문자 ≥ 1
    - 중간: 길이 ≥ 7, 숫자 ≥ 1, 대문자 ≥ 1, 특수문자 ≥ 1
    - 약함: 길이 ≥ 5
    """
    length = len(password)
    num_digits = sum(char.isdigit() for char in password)
    num_uppercase = sum(char.isupper() for char in password)
    num_special = sum(char in "!@#$%^&*" for char in password)

    if length >= 9 and num_digits >= 2 and num_uppercase >= 2 and num_special >= 1:
        return "강함"
    elif length >= 7 and num_digits >= 1 and num_uppercase >= 1 and num_special >= 1:
        return "중간"
    elif length >= 5:
        return "약함"
    else:
        return "보안 등급 없음"

# 메인 함수
def main():
    """
    프로그램의 메인 흐름을 담당하는 함수.
    - 사용자 입력: 비밀번호 개수, 포함/제외 문자, 보안등급
    - 출력: 생성된 비밀번호 및 보안등급
    """
    # 비밀번호 개수 입력
    numPasswords = getValidatedInput("몇 개의 비밀번호를 생성하시겠습니까? ")
    passwords = []

    # 사용자 정의 옵션 입력
    include_chars = input("모든 비밀번호에 반드시 포함할 문자를 입력하세요 (없으면 Enter): ")
    exclude_chars = input("모든 비밀번호에서 제외할 문자를 입력하세요 (없으면 Enter): ")

    # 비밀번호별 보안등급 선택
    strengths = []
    for i in range(1, numPasswords + 1):
        print(f"\n비밀번호 #{i}의 보안등급을 선택하세요:")
        print("1. 약함 (5 이상 7 미만)")
        print("2. 중간 (7 이상 9 미만)")
        print("3. 강함 (9 이상 12 미만)")
        choice = getValidatedInput("선택 (1-약함, 2-중간, 3-강함): ", valid_range=[1, 2, 3])
        strengths.append(["약함", "중간", "강함"][choice - 1])

    # 비밀번호 생성
    for i, strength in enumerate(strengths):
        passwords.append(generatePassword(strength, include_chars, exclude_chars))

    # 생성된 비밀번호 출력 및 재생성 여부 확인
    while True:
        print("\n생성된 비밀번호:")
        for i, password in enumerate(passwords, 1):
            strength = evaluatePasswordStrength(password)
            print(f"Password #{i}: {password} (보안등급: {strength})")

        regenerate = input("특정 비밀번호를 재생성하시겠습니까? (y/n): ").strip().lower()
        if regenerate == "y":
            # 재생성할 비밀번호 번호 입력
            index = getValidatedInput(f"재생성할 비밀번호 번호를 입력하세요 (1-{numPasswords}): ", valid_range=range(1, numPasswords + 1))
            passwords[index - 1] = generatePassword(strengths[index - 1], include_chars, exclude_chars)
            print(f"Password #{index}가 재생성되었습니다.")
        elif regenerate == "n":
            print("비밀번호 생성이 완료되었습니다.")
            break
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

if __name__ == "__main__":
    main()
