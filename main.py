import tools


def main():

    print("Choose the tool you want to use.\nPassword Generator(1) - AutoFilter(2)")

    tool = int(input("Enter a Number: "))
    if tool == 1:

        passgener.main()

    elif tool == 2:

        autofilter.main()
        print("Good to go!")


if __name__ == "__main__":
    main()
