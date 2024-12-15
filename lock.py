import random

def generatePassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*()_+[]"  # 특수문자 배열 추가
    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        password = replaceWithSpecialCharacter(password)  # 특수문자를 비밀번호에 추가하는 함수 호출
        
        passwords.append(password) 
    
    return passwords

def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword

def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword

def replaceWithSpecialCharacter(pword):
    # 특수문자를 비밀번호에 추가
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword))  # 특수문자를 삽입할 위치 랜덤 선택
        special_char = "!@#$%^&*()_+[]"  # 사용할 특수문자 목록
        pword = pword[:replace_index] + random.choice(special_char) + pword[replace_index + 1:]
    return pword

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = []
    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<3:
            length = 3
        passwordLengths.append(length)
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])

if __name__ == "__main__":
    main()

