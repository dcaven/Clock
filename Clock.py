# App1

#libraries
import time
import os

#vars
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
integers = [0,1,2,3,4,5,6,7,8,9]
asciiClock = [
    ["|__|", "|  |", " __ "], #zero
    ["   |", "   |", "    "], #one
    ["|__ ", " __|", " __ "], #two
    [" __|", " __|", " __ "], #three
    ["   |", "|__|", "    "], #four
    [" __|", "|__ ", " __ "], #five
    ["|__|", "|__ ", " __ "], #six
    ["   |", "   |", " __"], #seven
    ["|__|", "|__|", " __ "], #eight
    [" __|", "|__|", " __ "], #nine
    ["   ", " : " , "   "] #divider
]

#functions
def arrayToString(array):
    for x in array:
        print(x)
def stringToArray(string, delimiter):
    return string.split(delimiter)

def getInputAndYell():
    userInput = int(input("How badly did the bug hurt you (in number format)?\n"))
    message = "AH"
    count = 0
    while count < userInput:
        count += 1
        message += "H"
        if(count > 50):
            message += "\n"
            userInput -=50
            count = 0
    print(message)
def getCurrentDateTimeString():
    return str(str(time.localtime().tm_mday) + "-" + str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_year) + "  " + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
def getCurrentTime():
    return [time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec]
def startAsciiClock():
    level = 2
    currentTime = getCurrentTime()
    debug = False
    if(debug):
        print(currentTime)
        print(str(int(currentTime[0] / 10)) + "hour")
        print(str(int(currentTime[0] % 10)) + "hour")
        print(str(int(currentTime[1] / 10)) + "minute")
        print(str(int(currentTime[1] % 10)) + "minute")
        print(str(int(currentTime[2] / 10)) + "second")
        print(str(int(currentTime[2] % 10)) + "second")
    while level >= 0:
        levelstr = ""
        if(currentTime[0] < 10):
            levelstr += asciiClock[0][level] #zero
        else:
            levelstr += asciiClock[int(currentTime[0] / 10)][level] #hour column 1
        levelstr += asciiClock[int(currentTime[0] % 10)][level] #hour column 2
        levelstr += asciiClock[10][level] #divider
        if(currentTime[1] < 10):
            levelstr += asciiClock[0][level] #zero
        else:
            levelstr += asciiClock[int(currentTime[1] / 10)][level] #minute column 1
        levelstr += asciiClock[int(currentTime[1] % 10)][level] #minute column 2
        levelstr += asciiClock[10][level] #divider
        if(currentTime[2] < 10):
            levelstr += asciiClock[0][level] #zero
        else:
            levelstr += asciiClock[int(currentTime[2] / 10)][level] #second column 1
        levelstr += asciiClock[int(currentTime[2] % 10)][level] #second column 2
        print(levelstr)
        level -=1
    time.sleep(1)
    os.system('cls')


        

        

#main
# print("Hello World")
# print("\n")
# arrayToString(["Hi", "World."])
# print(stringToArray("Hi, World. Split this string", " "))
# getInputAndYell()
# print(getCurrentDateTimeString())
while 1:
    startAsciiClock()
