import random

def generatePassword(minLength, maxLength, numPasswords):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = [] 
    for i in range(numPasswords):
        length = random.randint(minLength, maxLength)
        password = "" 
        for j in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
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


def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " +str(numPasswords)+" passwords")
    minLength = int(input("Enter the minimum length of the password: "))
    maxLength = int(input("Enter the maximum length of the password: "))
    Password = generatePassword(minLength, maxLength, numPasswords)
    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])


if __name__ == '__main__':
    main()
