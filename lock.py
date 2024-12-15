import random

# 비밀번호를 생성하는 함수
def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwlength:
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
    # 특수문자를 추가하는 함수
    # 1. 사용할 특수문자들을 정의합니다.
    special_characters = "!@#$%^&*"

    # 2. 비밀번호 문자열에서 무작위 위치를 선택해 특수문자로 교체합니다.
    # 이 작업을 1번 또는 2번 반복합니다.
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword))  # 무작위 위치 선택
        selected_char = random.choice(special_characters)  # 특수문자 중 하나를 무작위로 선택
        pword = pword[0:replace_index] + selected_char + pword[replace_index+1:]  # 선택된 위치의 문자를 특수문자로 교체

    # 3. 특수문자가 추가된 비밀번호를 반환합니다.
    return pword

# 프로그램의 메인 함수
def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    passwordLengths = []

    print("Minimum length of password should be 3")
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)
    
    # 비밀번호를 생성
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i+1) + " = " + Password[i])

# 메인 함수 실행
if __name__ == "__main__":
    main()

