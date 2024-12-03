# Author: GitZamp
# *Important Message*: Be aware of the comments I leave. Usually they start with hashtag (#example) for single line comments or apostrophe ('''example''') for multiple lines of comments.

# Imports the build-in library 'random'.
import random

def main():
    def generate_password(pwlength):
        # Modern Latin Alphabet.
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        passwords = []
        # This {for} loop mixes the password with letters from the alphabet.
        for x in pwlength:

            password = ""
            for y in range(x):
                next_letter_index = random.randrange(len(alphabet))
                password = password + alphabet[next_letter_index]

            # The 2 lines below call the fuctions "replace_with_number" and "replace_with_uppercase_letter", (line 31 and line 37 respectively).
            password = replace_with_number(password)
            password = replace_with_uppercase_letter(password)

            passwords.append(password)

        return passwords

# This functions mixes the given password with random numbers.


    def replace_with_number(pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2)
            pword = pword[0:replace_index] + \
                str(random.randrange(10)) + pword[replace_index + 1:]
            return pword

# This function mixes the given password with Uppercase letters.


    def replace_with_uppercase_letter(pword):
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(pword) // 2, len(pword))
            pword = pword[0:replace_index] + \
                pword[replace_index].upper() + pword[replace_index + 1:]
            return pword
    print("How many passwords do you to generate?")
    num_passwords = int(input("Enter a Number: "))

    passwords_lengths = []
    # This {for} loop sets the length of the passwords according to your answer.
    for i in range(num_passwords):
        length = int(input("Set the length of password #" +
                     str(i + 1) + " [Min=3 & Max=16]: "))
        if length < 3:
            length = 3
        if length > 16:
            length = 16

        passwords_lengths.append(length)

    # Calls 'generate_password' fuction (line 8).
    password = generate_password(passwords_lengths)

    # This {for} loop prints the randomized passwords you want.
    for i in range(num_passwords):
        print("Password " + str(i + 1) + " = " + password[i])
