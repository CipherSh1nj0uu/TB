#
# Author: CipherSh1nj0u
#

import random


def generate_password(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = []

    for x in pwlength:

        password = ""
        for y in range(x):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        passwords.append(password)

    return passwords


def replace_with_number(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
        return pword


def replace_with_uppercase_letter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
        return pword


def main():
    num_passwords = int(input("posa passwords thes na kanw generate?? "))

    passwords_lengths = []

    for i in range(num_passwords):
        length = int(input("Bale to length tou password #" + str(i + 1) + " "))
        if length < 3:
            length = 3

        passwords_lengths.append(length)

    password = generate_password(passwords_lengths)

    for i in range(num_passwords):
        print("password " + str(i + 1) + " = " + password[i])


main()
