import random

# 비밀번호를 생성하는 함수
def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwlength:
        # 5글자 미만인 경우 에러 메시지 출력 후 넘어감
        if i < 5:
            print("Error: 5글자 미만의 비밀번호는 보안에 취약합니다. (요청한 길이:", i, ")")
            passwords.append("Error")
            continue

        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        # 숫자를 비밀번호에 추가
        password = replaceWithNumber(password)

        # 대문자를 비밀번호에 추가
        password = replaceWithUppercaseLetter(password)

        # 특수문자를 비밀번호에 추가
        password = replaceWithSpecialCharacter(password)

        passwords.append(password)

    return passwords

# 비밀번호 문자열에 숫자를 추가하는 함수
def replaceWithNumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword

# 비밀번호 문자열에 대문자를 추가하는 함수
def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword)//2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword

# 비밀번호 문자열에 특수문자를 추가하는 함수
def replaceWithSpecialCharacter(pword):
    special_characters = "!@#$%^&*"
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword))
        selected_char = random.choice(special_characters)
        pword = pword[0:replace_index] + selected_char + pword[replace_index+1:]
    return pword

# 비밀번호 보안등급을 평가하는 함수
def evaluatePasswordStrength(password):
    """
    비밀번호의 보안등급을 평가하는 함수

    - 강함: 길이가 12자 이상이고, 숫자, 대문자, 특수문자가 모두 포함된 경우
    - 중간: 길이가 8자 이상 12자 미만이고, 숫자, 대문자, 특수문자 중 두 가지 이상 포함된 경우
    - 약함: 길이가 8자 미만이거나, 숫자, 대문자, 특수문자 중 한 가지 이하만 포함된 경우
    """
    # 비밀번호의 길이를 계산
    length = len(password)

    # 비밀번호에 숫자가 포함되어 있는지 확인
    has_number = any(char.isdigit() for char in password)

    # 비밀번호에 대문자가 포함되어 있는지 확인
    has_uppercase = any(char.isupper() for char in password)

    # 비밀번호에 특수문자가 포함되어 있는지 확인
    has_special = any(char in "!@#$%^&*" for char in password)

    # 강함 조건
    if length >= 12 and has_number and has_uppercase and has_special:
        return "강함"

    # 중간 조건
    elif length >= 8 and sum([has_number, has_uppercase, has_special]) >= 2:
        return "중간"

    # 약함 조건
    else:
        return "약함"

# 프로그램의 메인 함수
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    passwordLengths = []

    print("Minimum length of password should be 5")
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        passwordLengths.append(length)

    while True:
        # 비밀번호를 생성
        Password = generatePassword(passwordLengths)

        # 결과 출력
        for i in range(numPasswords):
            if Password[i] == "Error":
                print(f"Password #{i + 1} = Error: 비밀번호 생성 실패 (길이 부족)")
            else:
                strength = evaluatePasswordStrength(Password[i])
                print(f"Password #{i + 1} = {Password[i]} (보안등급: {strength})")

        # 추가된 코드: 비밀번호 재설정 여부 확인
        # 사용자에게 비밀번호를 재설정할지 여부를 묻는 코드
        while True:
            # 사용자에게 재설정 여부를 묻는 메시지 출력
            regenerate = input("비밀번호를 다시 생성하시겠습니까? (y/n): ").strip().lower()

            # 사용자가 'y'를 입력한 경우
            if regenerate == "y":
                # 비밀번호 재생성을 위해 반복문을 계속 진행
                print("비밀번호를 다시 생성합니다.")
                break  # 내부 루프를 종료하여 비밀번호 재생성 루프로 이동

            # 사용자가 'n'을 입력한 경우
            elif regenerate == "n":
                # 재생성을 종료하고 전체 프로그램을 종료할 준비
                print("비밀번호 생성이 완료되었습니다.")
                return  # 프로그램 종료

            # 사용자가 잘못된 입력을 한 경우
            else:
                # 잘못된 입력임을 알리고 다시 입력하도록 유도
                print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

# 메인 함수 실행
if __name__ == "__main__":
    main()

