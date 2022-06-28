from random import*
def main():
    x = ""
    ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?@#$%^&*()-=_+"
    length = int(input("How long should your password be? "))
    for i in range (1, length+1):
        x += choice(ch)
    print("your password is:",x)
    o = input("PRESS [ENTER] FOR ANOTHER PASSWORD")
    if o == "":
        main()
    else:
        exit()
main()
