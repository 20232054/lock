import random

# 비밀번호 생성 함수
def generatePassword(strength="중간", include_chars="", exclude_chars=""):
    """
    선택한 보안등급(strength)에 따라 비밀번호를 생성하며,
    사용자가 지정한 문자를 포함하거나 제외할 수 있습니다.
    - 약함: 5 이상 7 미만
    - 중간: 7 이상 9 미만
    - 강함: 9 이상 12 미만
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*"
    password = ""

    # 비밀번호 길이 설정
    if strength == "약함":
        length = random.randint(5, 6)  # 5 이상 7 미만
    elif strength == "중간":
        length = random.randint(7, 8)  # 7 이상 9 미만
    elif strength == "강함":
        length = random.randint(9, 11)  # 9 이상 12 미만

    # 기본 문자 풀 생성
    char_pool = alphabet + alphabet.upper() + "0123456789" + special_characters

    # 제외할 문자를 필터링
    for char in exclude_chars:
        char_pool = char_pool.replace(char, "")

    # 강도별 비밀번호 생성
    for _ in range(length):
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

    if length >= 9 and length < 12 and has_number and has_uppercase and has_special:
        return "강함"
    elif length >= 7 and length < 9 and sum([has_number, has_uppercase, has_special]) >= 2:
        return "중간"
    elif length >= 5 and length < 7:
        return "약함"
    else:
        return "보안 등급 없음"

# 사용자 입력 함수
def getUserInputs(numPasswords):
    strengths = []
    for i in range(1, numPasswords + 1):
        print(f"\n비밀번호 #{i}의 보안등급을 선택하세요:")
        print("1. 약함 (5 이상 7 미만)")
        print("2. 중간 (7 이상 9 미만)")
        print("3. 강함 (9 이상 12 미만)")

        while True:
            try:
                choice = int(input("선택 (1-약함, 2-중간, 3-강함): "))
                if choice == 1:
                    strengths.append("약함")
                elif choice == 2:
                    strengths.append("중간")
                elif choice == 3:
                    strengths.append("강함")
                else:
                    print("1, 2, 3 중에서 선택해주세요.")
                    continue
                break
            except ValueError:
                print("숫자로 입력해주세요.")

    return strengths

# 메인 함수
def main():
    numPasswords = int(input("몇 개의 비밀번호를 생성하시겠습니까? "))
    passwords = []

    # 사용자 정의 옵션 입력
    include_chars = input("모든 비밀번호에 반드시 포함할 문자를 입력하세요 (없으면 Enter): ")
    exclude_chars = input("모든 비밀번호에서 제외할 문자를 입력하세요 (없으면 Enter): ")

    # 각 비밀번호의 보안등급 입력
    strengths = getUserInputs(numPasswords)

    for i, strength in enumerate(strengths):
        passwords.append(generatePassword(strength, include_chars, exclude_chars))

    while True:
        print("\n생성된 비밀번호:")
        for i, password in enumerate(passwords, 1):
            strength = evaluatePasswordStrength(password)
            print(f"Password #{i}: {password} (보안등급: {strength})")

        regenerate = input("특정 비밀번호를 재생성하시겠습니까? (y/n): ").strip().lower()
        if regenerate == "y":
            try:
                index = int(input(f"재생성할 비밀번호 번호를 입력하세요 (1-{numPasswords}): "))
                if 1 <= index <= numPasswords:
                    passwords[index - 1] = generatePassword(strengths[index - 1], include_chars, exclude_chars)
                    print(f"Password #{index}가 재생성되었습니다.")
                else:
                    print(f"Error: 1에서 {numPasswords} 사이의 번호를 입력하세요.")
            except ValueError:
                print("Error: 숫자를 입력하세요.")
        elif regenerate == "n":
            print("비밀번호 생성이 완료되었습니다.")
            break
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

if __name__ == "__main__":
    main()

