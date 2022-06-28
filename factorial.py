def main():
    x = int(input("The factorial of which number? "))
    y=1
    for i in range (2, x + 1):
         y *= i
    print(y)
    a = input("PRESS [ENTER] for relaunch")
    if a == "":
        main()
    else:
        exit()
main()
