import random
import time
score=0
fails=0
timeLimit=int(input("How many seconds to play do you want?"))
timeBegin=time.time()
while time.time()-timeBegin<timeLimit:
    operatorReal=random.randint(1,4)
    if operatorReal == 1:
        number1=random.randint(-100,100)
        number2=random.randint(-100,100)
        answer=number1+number2
        userAnswer1 = input(f"What is {number1} plus {number2}?")
        userAnswer = int(userAnswer1)
        if userAnswer == answer:
                 score = score +1
                 print("Right!")
        else:
                 fails = fails +1
                 print("Wrong")
    elif operatorReal==2:
        number1 = random.randint(-100, 100)
        number2 = random.randint(-100, 100)
        answer=number1-number2
        userAnswer1 =input(f"What is {number1} minus {number2}?")
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
         userAnswer1 = input(f"What is {number1} times {number2}?")
         userAnswer = int(userAnswer1)
         if userAnswer == answer:
             score = score + 1
             print("Right!")
         else:
             fails = fails + 1
             print("Wrong!")
    elif operatorReal == 4:
        answer=random.randint(1,12)
        number2=random.randint(1,12)
        number1=number2*answer
        userAnswer1 =input(f"What is {number1} divided by {number2}?")
        userAnswer=int(userAnswer1)
        if userAnswer == answer:
            score=score+1
            print("Correct!")
        else:
            fails=fails+1
            print("Wrong!")
print("Times up!")
if score+fails > 0:
    print(f"You got {score} questions right!")
    print(f"You got {fails} questions wrong...")
    totalAnswered=score+fails
    averageTime=timeLimit/totalAnswered
    print(f"On average, you answered a question every {averageTime} seconds.")
    accuracy=score/totalAnswered
    accuracy=accuracy*100
    accuracy=round(accuracy, 2)
    print(f"You answered {accuracy}% questions correctly!")
else:
    print("You didn't answer any questions!")



