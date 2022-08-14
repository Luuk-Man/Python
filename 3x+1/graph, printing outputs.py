from matplotlib.pyplot import*
def main():
    numb = int(input("For which number do you want to play '3x+1'?: "))
    num = numb
    x = []                    
    y=[]
    xas=0
    while True: 
        if num==1:
            print("Loop Found!")
            break
        elif num%2==0:
            num= num/2
            print(num)
        elif num%2==1:
            num = (3*num+1)
            print(num)
        yas=num
        xas+=1
        x.append(xas)
        y.append(yas)
    print("Loop found with number:",numb)
    xas = str(xas)
    input()
    plot(x,y)
    title("Het aantal iteraties is " + xas)
    xlabel("x-as")
    ylabel("y-as")
    show()
main()
