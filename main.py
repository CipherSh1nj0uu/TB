from tools import passgener
def main():
    print("\nMokzz: Welcome to my very first...primitive toolbox! You can use this set of tools however you want!\nMokzz: Choose the tool you want to use. (Password Generator(1) - AutoFilter(2))")
    tool=int(input("Me: "))
    if tool==1:
        passgener.main()
main()