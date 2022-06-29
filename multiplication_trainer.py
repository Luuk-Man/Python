from random import*
def main():
    good = 0
    bad = 0
    lowest = int(input("What's the lowest?: "))
    highest = int(input("What's the highest?: "))
    times = int(input("how many times?: "))
    for i in range (0,times):
        m1 = randrange(lowest,highest)
        m2 = randrange(lowest,highest)
        print('What is',m1,'times',str(m2)+'?')
        ans = int(input(""))
        if ans == m1 * m2:
            print("Good job!")
            good+=1
        else: 
            print("Not quite!")
            print("the answer should be:", str(m1*m2)+"!")
            bad+=1
    print(bad, "bad answerds given")
    print(good,"good answers given")
    repeat = input("PRESS [ENTER] TO PLAY AGAIN!")
    if repeat == "":
        main()
    else:
        exit()
main()
