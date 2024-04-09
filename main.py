from Tools import PasswordGenerator
from Tools import AutoFIlter
def main():
    print("\nMokzz: Welcome to my very first...primitive toolbox! You can use this set of tools however you want!\nMokzz: Choose the tool you want to use.\nPassword Generator(1) - AutoFilter(2)")
    tool=int(input("Me: "))
    if tool==1:
        PasswordGenerator.main()
    elif tool==2:
        AutoFIlter.main()
        print("Good to go!")
if __name__=="__main__":
    main()