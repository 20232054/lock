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

# 프로그램의 메인 함수
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    passwordLengths = []

    print("Minimum length of password should be 5")
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        passwordLengths.append(length)

    # 비밀번호를 생성
    Password = generatePassword(passwordLengths)

    # 결과 출력
    for i in range(numPasswords):
        if Password[i] == "Error":
            print("Password #" + str(i+1) + " = Error: 비밀번호 생성 실패 (길이 부족)")
        else:
            print("Password #" + str(i+1) + " = " + Password[i])

# 메인 함수 실행
if __name__ == "__main__":
    main()

