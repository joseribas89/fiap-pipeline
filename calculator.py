import random

def generatePassword(lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []
    for length in lengths:
        if length < 3:
            length = 3
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

    numPasswords = 5
    minLength = 3
    maxLength = 10

    print("Generating " + str(numPasswords) + " passwords")

    passwords = generatePassword(numPasswords, minLength, maxLength)

    for i in range(numPasswords):
        print("Password #" + str(i+1) + " = " + passwords[i])


main()
