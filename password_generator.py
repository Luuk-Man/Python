from random import choice
def main():
    a = ""
    while a == "":
        pw = "" #empty password
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?@#$%^&*()-=_+" #characters possible in given password
        l = int(input("How long should your password be? ")) #ask for password lenght
        for i in range (0, l):pw += choice(ch) #make random password
        print("your password is:",pw) #say password
        a = input("PRESS [ENTER] FOR ANOTHER PASSWORD")
    exit()
main()
