import time
def tenSeconds():
    input("Press enter to begin the game, then press enter once you believe 10 seconds have passed.")
    start=time.time()
    input("Enter to finish")
    end=time.time()
    time_elapsed=end-start
    time_elapsed=(round(time_elapsed, 3))
    print("You took", time_elapsed, "seconds!")
    if time_elapsed>9 and time_elapsed<11:
        print("Good job!")


def customSeconds(custom):
    customButSTR = str(custom)
    input("Press enter to begin the game, then press enter once you believe " + customButSTR+  " seconds have passed.")
    start=time.time()
    input("Enter to finish")
    end=time.time()
    time_elapsed=end-start
    time_elapsed=(round(time_elapsed, 3))
    print("You took", time_elapsed, "seconds!")
    if time_elapsed>custom-1 and time_elapsed<custom+1:
        print("Good job!")


def fiveSeconds():
    input("Press enter to begin the game, then press enter once you believe 5 seconds have passed.")
    start=time.time()
    input("Enter to finish")
    end=time.time()
    time_elapsed=end-start
    time_elapsed=(round(time_elapsed, 3))
    print("You took", time_elapsed, "seconds!")
    if time_elapsed>4 and time_elapsed<6:
        print("Good job!")


def fifteenSeconds():
    input("Press enter to begin the game, then press enter once you believe 15 seconds have passed.")
    start=time.time()
    input("Enter to finish")
    end=time.time()
    time_elapsed=end-start
    time_elapsed=(round(time_elapsed, 3))
    print("You took", time_elapsed, "seconds!")
    if time_elapsed>14 and time_elapsed<16:
        print("Good job!")


done=0
while done==0:
    whatGame=input("What waiting game would you like to play? 5 seconds, 10 seconds, 15 seconds, or a custom amount of time?")
    if whatGame == "custom" or whatGame=="Custom":
        custom = int(input("How long?"))
        if isinstance(custom, str):
            print("This is an invalid input.")
        else:
            customSeconds(custom)
    else:
        whatGame=int(whatGame)
        if whatGame == 5:
          fiveSeconds()
        elif whatGame == 10:
          tenSeconds()
        elif whatGame == 15:
          fifteenSeconds()