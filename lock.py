import random

# 비밀번호 생성 함수
def generatePassword(strength="중간", include_chars="", exclude_chars=""):
    """
    선택한 보안등급(strength)에 따라 비밀번호를 생성하며,
    사용자가 지정한 문자를 포함하거나 제외할 수 있습니다.
    - 약함: 5~7자리, 소문자만 포함
    - 중간: 7~9자리, 소문자, 숫자, 대문자 중 두 가지 포함
    - 강함: 9~12자리, 소문자, 숫자, 대문자, 특수문자 모두 포함
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*"
    password = ""

    # 비밀번호 길이 설정
    if strength == "약함":
        length = random.randint(5, 6)
    elif strength == "중간":
        length = random.randint(7, 8)
    elif strength == "강함":
        length = random.randint(9, 11)

    # 기본 문자 풀 생성
    char_pool = alphabet + alphabet.upper() + "0123456789" + special_characters

    # 제외할 문자를 필터링
    for char in exclude_chars:
        char_pool = char_pool.replace(char, "")

    # 강도별 비밀번호 생성
    for _ in range(length - len(include_chars)):
        password += random.choice(char_pool)

    # 사용자가 포함하고 싶은 문자를 비밀번호에 추가
    password += include_chars

    # 강함일 경우 특수문자와 대문자를 보장
    if strength == "강함":
        password = replaceWithSpecialCharacter(password)
        password = replaceWithUppercaseLetter(password)

    # 비밀번호를 랜덤하게 섞기
    password = ''.join(random.sample(password, len(password)))

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
    length = len(password)
    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)

    if length >= 9 and has_number and has_uppercase and has_special:
        return "강함"
    elif length >= 7 and sum([has_number, has_uppercase, has_special]) >= 2:
        return "중간"
    else:
        return "약함"

# 사용자 입력 검증 함수
def getValidatedInput(prompt, valid_range=None):
    """
    사용자 입력을 검증하는 함수.
    - prompt: 입력 요청 메시지
    - valid_range: 유효한 입력값의 범위 (리스트나 튜플)
    """
    while True:
        try:
            user_input = int(input(prompt))
            if valid_range and user_input not in valid_range:
                print(f"Error: {valid_range[0]}에서 {valid_range[-1]} 사이의 숫자를 입력하세요.")
                continue
            return user_input
        except ValueError:
            print("Error: 숫자를 입력하세요.")

# 메인 함수
def main():
    """
    프로그램의 메인 함수
    - 비밀번호 개수, 보안등급, 사용자 정의 문자 포함/제외 기능 제공
    - 생성된 비밀번호 출력 및 특정 비밀번호 재생성 기능 제공
    """
    print("비밀번호 생성 프로그램입니다.")
    numPasswords = getValidatedInput("몇 개의 비밀번호를 생성하시겠습니까? ")
    passwords = []

    # 사용자 정의 문자 입력
    include_chars = input("모든 비밀번호에 반드시 포함할 문자를 입력하세요 (없으면 Enter): ")
    exclude_chars = input("모든 비밀번호에서 제외할 문자를 입력하세요 (없으면 Enter): ")

    # 보안등급 선택
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

    # 출력 형식 개선
    while True:
        print("\n생성된 비밀번호:")
        print(f"{'번호':<5} {'비밀번호':<20} {'보안등급':<10}")
        print("=" * 40)
        for i, password in enumerate(passwords, 1):
            strength = evaluatePasswordStrength(password)
            print(f"{i:<5} {password:<20} {strength:<10}")

        # 특정 비밀번호 재생성
        regenerate = input("특정 비밀번호를 재생성하시겠습니까? (y/n): ").strip().lower()
        if regenerate == "y":
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

