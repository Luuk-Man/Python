def main():
    r = ""                                                  #initialize the restart variable
    l = [1]                                                 #initialize the list l with 1
    while r == "":                                          #while user hasn't stopped the program
        n = int(input("The factorial of which number? "))       #ask user for an input and call it n
        if n < len(l): print(l[n])                              #if n is in l: print it directly
        else:                                                   #else calculate new f:
            f = l[len(l)-1]                                         #initialize f as the last item in the list
            for i in range (len(l), n+1):                           #cycle i through every number from the lenght of l to n.
                f *= i                                                  #multiply f by i
                l.append(f)                                             #add f to the list
            print(f)                                                #print freshly calculated factorial
        r = input("PRESS [ENTER] for relaunch")                 #ask the user to pres [ENTER] to relaunch
    exit()                                                  #if the user stopped the program exit
main()
