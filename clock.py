from time import*
def main():
    uur = int(input("Hoeveel uur? "))
    min = int(input("Hoeveel minuten? "))
    sec = int(input("Hoeveel seconden? "))
    while True:
        print(uur,":", min,":",sec)
        sec = sec + 1
        if sec == 60:
            sec = 0
            min = min + 1
        if min == 60:
            min = 0
            uur = uur + 1
        if uur == 24:
            uur = 0
        sleep(1)
main()