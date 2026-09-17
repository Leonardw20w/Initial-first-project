import random
import time
score=0
fails=0
timeLimit=int(input("How many seconds to play do you want?"))
timeBegin=time.time()
while time.time()-timeBegin<timeLimit:
    operatorReal=random.randint(1,4)
    if operatorReal == 1 or operatorReal == 2:
        number1=random.randint(-100,100)
        number2=random.randint(-100,100)
        if operatorReal ==1:
             answer=number1+number2
             number11 = str(number1)
             number22 = str(number2)
             userAnswer1 = input(f"What is " + number11 + " plus " + number22 + "?")
             userAnswer = int(userAnswer1)
             if userAnswer == answer:
                 score = score + 1
                 print("Right!")
             else:
                fails = fails + 1
                print("Wrong")
        else:
             answer=number1-number2
             number11 = str(number1)
             number22 = str(number2)
             userAnswer1 =input(f"What is " + number11 + " minus " + number22 + "?")
             userAnswer=int(userAnswer1)
        if userAnswer == answer:
            score = score + 1
            print("Right!")
        else:
            fails=fails+1
            print("Wrong")
    elif operatorReal == 3:
         number1=random.randint(-12,12)
         number2=random.randint(-12,12)
         answer=number1*number2
         number11 = str(number1)
         number22 = str(number2)
         userAnswer1 = input(f"What is " + number11 + " times " + number22 + "?")
         userAnswer = int(userAnswer1)
         if userAnswer == answer:
             score = score + 1
             print("Right!")
         else:
             fails = fails + 1
             print("Wrong!")
    elif operatorReal == 4:
        solvable="false"
        while solvable=="false":
            number1 = random.randint(1, 100)
            number2 = random.randint(1, 12)
            answer=number1/number2
            #checking if question is solvable
            if isinstance(answer, int):
                solvable="true"
        number11=str(number1)
        number22=str(number2)
        userAnswer1 =input(f"What is " + number11 + " divided by " + number22 + "?")
        userAnswer=int(userAnswer1)
        if userAnswer == answer:
            score=score+1
            print("Correct!")
        else:
            fails=fails+1
            print("Wrong!")
print("Times up!")
scorePrint=str(score)
print("You got "+ scorePrint+ " questions right!")
failprint=str(fails)
print("You got "+ failprint+" questions wrong...")
totalAnswered=score+fails
averageTime=totalAnswered/timeLimit
averageTimePrint=str(averageTime)
print("On average, you answered a question every "+ averageTimePrint + " seconds.")
accuracy=totalAnswered/score
failAccuracy=100-accuracy
failAccuracyPrint=str(failAccuracy)
accuracyPrint=str(accuracy)
print("You answered "+ accuracyPrint + "% questions correctly and "+failAccuracyPrint+"% incorrectly")



