from random import*
from decimal import*
getcontext().prec = 3
def main():
	bad = 0
	good = 0
	questionType = "idk"
	typeList = ["m","d","a","s"]
	wordList = ["Multiplication","Division","Addition","Subtraction"]
	questionWordList = [" times "," divided by "," plus "," minus "]
	while not(questionType in typeList):
		print("Question types in program:")
		for i in range (0,len(typeList)):print (typeList[i]+": "+wordList[i])
		questionType = str(input("What do you want to train?"))
	questionTypeIndex = typeList.index(questionType)
	lowest = int(input("What's the lowest?: "))
	highest = int(input("What's the highest?: "))+1
	times = int(input("how many times?: "))
	for i in range (0,times):
		n1 = Decimal(randrange(lowest,highest))
		n2 = Decimal(randrange(lowest,highest))
		ans = Decimal(input('What is '+str(n1)+str(questionWordList[questionTypeIndex])+str(n2)+' ? '))
		if   questionType == "m": correct = n1*n2
		elif questionType == "d": correct = n1/n2
		elif questionType == "a": correct = n1+n2
		elif questionType == "s": correct = n1-n2
		if ans == correct:
			print("Good job!")
			good+=1
		else:
			print("Not quite!")
			print("the answer should be: "+str(correct)+" !")
			bad+=1
	print(bad, "bad answerds given")
	print(good,"good answers given")
	repeat = input("PRESS [ENTER] TO PLAY AGAIN!")
	if repeat == "":
		main()
	else:
		exit()
main()
