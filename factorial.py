def main():
    a = ""
    while a == "":
        f = 1
        n = int(input("The factorial of which number? "))
        for i in range (2, n + 1):f *= i #multiplies f by every number from 2 to n
        print(f)
        a = input("PRESS [ENTER] for relaunch")
main()
