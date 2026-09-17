import random
import time

def gamestart():
    timeLimit=int(input("How many seconds to play do you want?"))
    timeBegin=time.time()
    while time.time()-timeBegin<timeLimit:
        operatorReal=random.randint(1,4)
        if operatorReal == 1 or operatorReal == 2:
            number1=random.randint(-100,100)
            number2=random.randint(-100,100)
            if operatorReal ==1:
                answer=number1+number2
            else:
                answer=number1-number2
        elif operatorReal == 3:
            number1=random.randint(-12,12)
            number2=random.randint(-12,12)
        ekif operatorReal == 4:

    print("Times up!")

