import random

def generatePassword(pwlength, strength="중간"):
    """
    선택한 보안등급(strength)에 따라 비밀번호를 생성하는 함수

    - 약함: 5~7자리, 소문자만 포함
    - 중간: 8~11자리, 소문자, 숫자, 대문자 중 두 가지 포함
    - 강함: 12자리 이상, 소문자, 숫자, 대문자, 특수문자 모두 포함
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*"
    password = ""

    # 비밀번호 길이 설정
    if strength == "약함":
        length = random.randint(5, 7)
    elif strength == "중간":
        length = random.randint(8, 11)
    elif strength == "강함":
        length = max(pwlength, 12)  # 강함은 최소 12자 이상

    # 강도별 비밀번호 생성
    for _ in range(length):
        if strength == "약함":
            password += random.choice(alphabet)  # 소문자만
        elif strength == "중간":
            password += random.choice(alphabet + alphabet.upper() + "0123456789")  # 소문자, 대문자, 숫자
        elif strength == "강함":
            # 소문자, 대문자, 숫자, 특수문자 모두 포함
            password += random.choice(alphabet + alphabet.upper() + "0123456789" + special_characters)

    # 강함일 경우, 추가적으로 특수문자와 대문자를 반드시 포함하도록 보정
    if strength == "강함":
        password = replaceWithSpecialCharacter(password)
        password = replaceWithUppercaseLetter(password)

    return password

def replaceWithSpecialCharacter(pword):
    """
    비밀번호에 랜덤 특수문자를 추가
    """
    special_characters = "!@#$%^&*"
    replace_index = random.randrange(len(pword))
    selected_char = random.choice(special_characters)
    return pword[:replace_index] + selected_char + pword[replace_index + 1:]

def replaceWithUppercaseLetter(pword):
    """
    비밀번호에 랜덤 대문자를 추가
    """
    replace_index = random.randrange(len(pword))
    return pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]

def main():
    print("비밀번호 생성 프로그램입니다.")
    print("원하는 보안등급을 선택하세요:")
    print("1. 약함")
    print("2. 중간")
    print("3. 강함")

    while True:
        try:
            strength_choice = int(input("선택 (1-약함, 2-중간, 3-강함): "))
            if strength_choice == 1:
                strength = "약함"
            elif strength_choice == 2:
                strength = "중간"
            elif strength_choice == 3:
                strength = "강함"
            else:
                print("1, 2, 3 중에서 선택해주세요.")
                continue
            break
        except ValueError:
            print("숫자로 입력해주세요.")

    numPasswords = int(input("몇 개의 비밀번호를 생성하시겠습니까? "))
    passwords = []

    for _ in range(numPasswords):
        if strength == "강함":
            length = int(input("강한 비밀번호의 길이를 입력하세요 (12 이상): "))
        else:
            length = 0  # 약함, 중간은 고정된 범위에서 랜덤하게 결정
        passwords.append(generatePassword(length, strength))

    print("\n생성된 비밀번호:")
    for i, password in enumerate(passwords, 1):
        print(f"Password #{i}: {password}")

if __name__ == "__main__":
    main()
